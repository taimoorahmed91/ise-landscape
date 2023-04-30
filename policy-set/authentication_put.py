import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#will accept policy srchref dsthref


srchref = sys.argv[1]
dsthref = sys.argv[2]
name = sys.argv[3]




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
response = requests.get(srchref, headers=headers, data=payload, verify=False)
#print(response.text)


json_response = response.json()
initial_result = json_response['response']
#print(initial_result)




#print(final_result)

del initial_result['rule']['id']
#print(initial_result)

final_result = json.dumps(initial_result)
#print("this is separation")
#print(final_result)

response_post = requests.request("PUT", dsthref, headers=headers, data=final_result, verify=False)
output = (response_post.text)
#print(output)
response_post = str(response_post)
response_post = response_post[:-1]
response_post = response_post[1:]
print(response_post)


cursor = connection.cursor(dictionary=True)
sql_update_query = """Update policysetauthen set code_put = %s where name = %s"""
input_data = (response_post, name)
cursor.execute(sql_update_query, input_data)
connection.commit()
