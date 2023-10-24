import mysql.connector
import sys

# Define the database credentials
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'C1sc0123@',
    'database': 'mise'
}

policyset1 = sys.argv[1]
isename1 = sys.argv[2]

policyset2 = sys.argv[3]
isename2 = sys.argv[4]

# Execute the first SQL query
query1 = f"SELECT authorization FROM `authorization` WHERE policyset = '{policyset1}' AND isename = '{isename1}'"

connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor(dictionary=True)

cursor.execute(query1)

result1 = cursor.fetchall()

cursor.close()

# Execute the second SQL query
query2 = f"SELECT authorization FROM `authorization` WHERE policyset = '{policyset2}' AND isename = '{isename2}'"

connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor(dictionary=True)

cursor.execute(query2)

result2 = cursor.fetchall()

cursor.close()
connection.close()

# Print the query results
print("Query 1 result:")
for row in result1:
    print(row["authorization"])

print("=================")

print("Query 2 result:")
for row in result2:
    print(row["authorization"])

print("=================")

# Find differences
differences = [item for item in result1 if item not in result2]

if differences:
    print("Differences found:")
    for diff in differences:
        print(diff["authorization"])
else:
    print("No differences found. Query results are identical.")
