import urllib3
import requests
import sys
import json
import mysql.connector
import contextlib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#will accept id , dstise ,dstpolicysetid and dstpolicyid


insertid = sys.argv[1]
dstise = sys.argv[2]
dstpolicysetid = sys.argv[3]
srcpolicyid = sys.argv[4]
dstpolicyid = sys.argv[5]


connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')




## create your URL first

authentication = "authentication"




firsthalfurl = "https://"
secondhalfurl = "/api/v1/policy/network-access/policy-set"


url = firsthalfurl + dstise + secondhalfurl + "/" + dstpolicysetid + "/" + authentication + "/" + dstpolicyid

print(url)


## open the file as fetched from the SQL data

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

#filename  = 'demofile'
filename = "/root/ise-landscape/policyset/authentications/" + srcpolicyid
#print(filename)

with open(f'{filename}', 'r', encoding='utf-8') as f:
    final_result = f.read()

#print(final_result)

#post the response


response_post = requests.request("PUT", url, headers=headers, data=final_result, verify=False)
output = (response_post.text)
#print(output)



json_response = response_post.json()
#print(json_response)




response_post = str(response_post)
response_post = response_post[:-1]
response_post = response_post[1:]
print(response_post)



cursor = connection.cursor(dictionary=True)
sql_update_query = """Update replicateauthentication set code_put = %s where id = %s"""
input_data = (response_post,insertid )
cursor.execute(sql_update_query, input_data)
connection.commit()




