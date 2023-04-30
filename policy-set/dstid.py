import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





id = sys.argv[1]




connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')
sql_select_Query = "select name from policyset where id = id"

cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


#print(records)



for row in records:
        policyset = row["name"]


#print(policyset)


url = "https://ise-proxy2.taimoorlab.local/api/v1/policy/network-access/policy-set"

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(url, headers=headers, data=payload, verify=False)

json_response = response.json()


#print(json.dumps(json_response))

for value in json_response['response']:
    if value['name'] == policyset:
        my_id=(value['id'])


#print(my_id)



## update to DB

## updates to be pushed to db are from here


cursor = connection.cursor(dictionary=True)
sql_update_query = """Update policyset set dstid = %s where id = %s"""
input_data = (my_id,id)
cursor.execute(sql_update_query, input_data)
connection.commit()







