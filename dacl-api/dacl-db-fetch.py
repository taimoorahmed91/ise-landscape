import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



connection = mysql.connector.connect(host='odbc.taimoorlab.local',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')
sql_select_Query = "select * from temp where expired = 'yes'"

cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


for row in records:
        dacl = row["dacl"]



#print(dacl)


url = "https://ise32.taimoorlab.local:9060/ers/config/downloadableacl/"

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(url, headers=headers, data=payload, verify=False)

json_response = response.json()


#print(json.dumps(json_response))

for value in json_response['SearchResult']['resources']:
    if value['name'] == dacl:
        my_id=(value['id'])


#print(my_id)
