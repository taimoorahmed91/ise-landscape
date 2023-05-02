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
        name=(value['name'])
        policyid=(value['id'])
        #print(name)
        cursor = connection.cursor(dictionary=True)
        sql_update_query = """INSERT INTO policy_dest (name,id) VALUES (%s,%s)"""
        input_data = (name,policyid)
        cursor.execute(sql_update_query, input_data)
        connection.commit()
