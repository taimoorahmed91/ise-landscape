import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')
sql_select_Query = "select * from authz where expired = 'no'"

cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


for row in records:
        authz = row["authz"]



#print(dacl)


url = "https://ise32.taimoorlab.local/ers/config/authorizationprofile/"

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
    if value['name'] == authz:
        my_id=(value['id'])


#print(my_id)



newurl = url + my_id

response2 = requests.request("GET", newurl, headers=headers, data=payload, verify=False)

result =(response2.text)

#print(result)

json_response2 = response2.json()
#print(json.dumps(json_response2))

#print(response2)



dacl_code = json_response2['AuthorizationProfile']['daclName']
#print(dacl_code)






## updates to be pushed to db are from here

#dacl_name = str(dacl_code)
#print(dacl_name)
print(authz)

cursor = connection.cursor(dictionary=True)
sql_insert_query = "INSERT INTO temp (dacl, authz, expired) VALUES (%s, %s,'no')"
val = (dacl_code, authz)
cursor.execute(sql_insert_query, val)
connection.commit(



        )
