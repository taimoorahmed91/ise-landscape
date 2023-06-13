import urllib3
import requests
import sys
import json
import mysql.connector
import contextlib
import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


connection = mysql.connector.connect(host='127.0.0.1',
                                     database='mise',
                                     user='root',
                                     password='C1sc0123@')

#will accept id , dstise and dstpolicysetid

insertid = sys.argv [1]
fqdn = sys.argv[2]
apid = sys.argv[3]


### set time parameters
current_time = datetime.datetime.now()

# Format the time as a string
time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")




firsthalfurl = "https://"
secondhalfurl = "/ers/config/allowedprotocols"


url = firsthalfurl + fqdn + secondhalfurl 

#print(url)


## open the file as fetched from the SQL data

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}


filename = "/var/www/html/mise/v0.1/configs/ap/" + apid
#print(filename)

with open(f'{filename}', 'r', encoding='utf-8') as f:
    final_result = f.read()

#print(final_result)


response_post = requests.request("POST", url, headers=headers, data=final_result, verify=False)
output = (response_post.text)
#print(output)


file_path = "/var/www/html/mise/v0.1/logging/ap-logs"
with open(file_path, "a") as file:
    # Append the output to the file
    file.write(time_string + "\n")
    file.write(output)



#json_response = response_post.json()
#print(json_response)


response_post = str(response_post)
response_post = response_post[:-1]
response_post = response_post[1:]
print(response_post)



cursor = connection.cursor(dictionary=True)
sql_update_query = """Update ap set post_code = %s where id = %s"""
input_data = (response_post,insertid )
cursor.execute(sql_update_query, input_data)
connection.commit()

#cursor = connection.cursor(dictionary=True)
#sql_update_query = """Update ap set queue = 'no' where id = %s"""
#input_data = (insertid, )
#cursor.execute(sql_update_query, input_data )
#connection.commit()
