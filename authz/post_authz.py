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




post_url ='https://ise-proxy2.taimoorlab.local/ers/config/authorizationprofile'


response_post = requests.request("POST", post_url, headers=headers, data=result, verify=False)
#print(response_post)


http_code = str(response_post)
http_code = http_code[:-1]
http_code = http_code[1:]
print(http_code)



## updates to be pushed to db are from here


cursor = connection.cursor(dictionary=True)
sql_update_query = """Update authz set code_post = %s where authz = %s"""
input_data = (http_code, authz)
cursor.execute(sql_update_query, input_data)
connection.commit()
