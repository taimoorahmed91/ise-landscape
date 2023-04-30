import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



#will accept policy name and dsturl





name = sys.argv[1] 
dsturl = sys.argv[2]


connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')




payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

responses = requests.get(dsturl, headers=headers, data=payload, verify=False)

result = (responses.text)
#print(result)


json_responses = responses.json()


#print(json.dumps(json_responses))

for value in json_responses['response']:
    if value['rule']['name'] == name:
        my_ref=(value['link']['href'])

print(my_ref)


cursor = connection.cursor(dictionary=True)
sql_update_query = """Update policysetauthen set dsthref = %s where name = %s"""
input_data = (my_ref, name)
cursor.execute(sql_update_query, input_data)
connection.commit()
