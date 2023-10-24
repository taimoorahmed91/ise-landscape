import mysql.connector
import sys
import time
import subprocess

# Get the current time in seconds since the epoch (as a float)
current_time_float = time.time()
authentication_value = ""

# Convert the float value to an integer
random = int(current_time_float)

file_name = f"authen_{random}.txt"
with open(file_name, "w") as file:
    file.write(f"This is your file result for comparison of authentication in policy set")
    file.write("\n\n")

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
query1 = f"SELECT authentication FROM `authentication` WHERE policyset = '{policyset1}' AND isename = '{isename1}'"

connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor(dictionary=True)

cursor.execute(query1)

result1 = cursor.fetchall()

cursor.close()

# Execute the second SQL query
query2 = f"SELECT authentication FROM `authentication` WHERE policyset = '{policyset2}' AND isename = '{isename2}'"

connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor(dictionary=True)

cursor.execute(query2)

result2 = cursor.fetchall()

cursor.close()
connection.close()

# Append the query results to the file
with open(file_name, "a") as file:
    file.write("Authentication Policies in ISE 1:\n")
    for row in result1:
        file.write(row["authentication"] + '\n')

    file.write("=================\n")

    file.write("Authentication Policies in ISE 2:\n")
    for row in result2:
        file.write(row["authentication"] + '\n')

    file.write("=================\n")

    # Find differences
    differences = [item for item in result1 if item not in result2]

    if differences:
        file.write("Differences found:\n")
        for diff in differences:
            file.write(diff["authentication"] + '\n')
    else:
        file.write("No differences found.\n")

    file.write("=================\n")

    # Find common elements
    common_elements = [item for item in result1 if item in result2]

    if common_elements:
        file.write("Common elements found:\n")
        for common in common_elements:
            file.write(common["authentication"] + '\n')
            authentication_value = common["authentication"]
            
            

        # Perform another select query for the common element
            additional_query1 = f"SELECT authenticationid FROM `authentication` WHERE authentication = '{common['authentication']}' AND isename = '{isename1}' AND policyset = '{policyset1}'"

            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            cursor.execute(additional_query1)
            additional_result = cursor.fetchall()
            cursor.close()
            connection.close()

            #file.write("=================\n")
            # Print the additional query result values only
            for additional_row in additional_result:
                for key, value in additional_row.items():
                    file.write(f" {value}\n")
                    if isinstance(value, str):
                        string_value1 = value

            additional_query2 = f"SELECT authenticationid FROM `authentication` WHERE authentication = '{common['authentication']}' AND isename = '{isename2}' AND policyset = '{policyset2}'"

            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            cursor.execute(additional_query2)
            additional_result = cursor.fetchall()
            cursor.close()
            connection.close()


        # Print the additional query result values only
            for additional_row in additional_result:
                for key, value in additional_row.items():
                 file.write(f" {value}\n")
                 if isinstance(value, str):
                        string_value2 = value

        # Insert values into the DB
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()

            insert_query = "INSERT INTO compareauthen (random, authentication, authenid1, authenid2) VALUES (%s, %s, %s, %s)"
            values = (random, authentication_value, string_value1, string_value2)
            try:
                cursor.execute(insert_query, values)
                connection.commit()
                #print("Data inserted successfully.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
                connection.close()
        
            file.write("=================\n")
    else:
        file.write("No common elements found.\n")

# Append 'random' to the file
with open(file_name, "a") as file:
    #file.write(str(random))
    file.write("\n")



# starting to compare files now




connection = mysql.connector.connect(**DB_CONFIG)
cursor = connection.cursor()



# SQL query to retrieve 'authentication', 'authenid1', and 'authenid2' based on 'random'
select_query = f"SELECT authentication, authenid1, authenid2 FROM compareauthen WHERE random = {random}"
cursor.execute(select_query)
records = cursor.fetchall()



try:
    cursor.execute(select_query)
    records = cursor.fetchall()

    # Define the path to the Python script you want to run
    script_to_run = "compare.py"

    with open(file_name, "a") as file:  # Use "a" mode for append
        for record in records:
            authentication, authenid1, authenid2 = record

            # Print the value of 'authentication' before running the script
            file.write(f"Authentication: {authentication}\n")

            # Command to run the sub-script with authenid1 and authenid2 as arguments
            command = ["python3", script_to_run, str(authenid1), str(authenid2)]

            try:
                subprocess.check_call(command, stdout=file)
            except subprocess.CalledProcessError as e:
                file.write(f"Error while running the script for authenid1: {authenid1}, authenid2: {authenid2}: {e}\n")
            except Exception as e:
                file.write(f"An error occurred for authenid1: {authenid1}, authenid2: {authenid2}: {e}\n")
            file.write("\n")

except mysql.connector.Error as err:
    with open(file_name, "a") as file:
        file.write(f"Error: {err}\n")
finally:
    cursor.close()
    connection.close()