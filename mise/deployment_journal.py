import json
import mysql.connector
from datetime import datetime

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='C1sc0123@',
    database='mise'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the SQL query
query = """
SELECT `ap` AS `name`, 'ap' AS `table_name` FROM ap WHERE `queue` = 'yes'
UNION ALL
SELECT `dacl` AS `name`, 'dacl' AS `table_name` FROM dacl WHERE `queue` = 'yes'

UNION ALL
SELECT `authz` AS `name`, 'authz' AS `table_name` FROM authz WHERE `queue` = 'yes'

UNION ALL
SELECT `sgt` AS `name`, 'sgt' AS `table_name` FROM sgt WHERE `queue` = 'yes'

UNION ALL
SELECT `nad` AS `name`, 'nad' AS `table_name` FROM nad WHERE `queue` = 'yes'
ORDER BY `table_name`;

"""

# Execute the SQL query
cursor.execute(query)

# Create a dictionary to store the table names and corresponding names
data = {}

# Fetch rows from the result and populate the data dictionary
for row in cursor.fetchall():
    name = row[0]
    table_name = row[1]
    
    if table_name not in data:
        data[table_name] = []
    
    data[table_name].append(name)

# Close the cursor and the database connection
cursor.close()
connection.close()

# Create a unique filename with date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"/var/www/html/landscape/deployments/deployment_{timestamp}.json"

# Write the data to a file in JSON format with indentation
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data written to {filename}")

