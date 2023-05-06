import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#will accept dstise and dstpolicyset

insertid = sys.argv[1]
dstise = sys.argv[2]
dstpolicyset = sys.argv[3]




connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')


first_half_url = "https://"
second_half_url = "/api/v1/policy/network-access/policy-set"

url = first_half_url + dstise + second_half_url
#print(url)


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
    if value['name'] == dstpolicyset:
        my_id=(value['id'])


print(my_id)




## update to DB

## updates to be pushed to db are from here


cursor = connection.cursor(dictionary=True)
sql_update_query = """Update replicateauthentication set dstpolicysetid = %s where id = %s"""
input_data = (my_id,insertid )
cursor.execute(sql_update_query, input_data)
connection.commit()

