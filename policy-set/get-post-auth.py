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
sql_select_Query = "select srcid,dstid from policyset where id = id"

cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


#print(records)



for row in records:
        srcid = row["srcid"]
        dstid = row["dstid"]


authentication = "authentication"

baseurl_src = "https://ise32.taimoorlab.local/api/v1/policy/network-access/policy-set"
baseurl_dst = "https://ise-proxy2.taimoorlab.local/api/v1/policy/network-access/policy-set"


srcurl = baseurl_src + "/" + srcid + "/" + authentication
dsturl = baseurl_dst + "/" + dstid + "/" + authentication

#print(srcurl)
#print(dsturl)


payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(srcurl, headers=headers, data=payload, verify=False)
result =(response.text)
#print(result)

json_response = response.json()

length = 100


i = 0
while i < length:
    my_id = json_response['response'][i]['rule']['id']
    #print(my_id)
    srcauthurl = srcurl + "/" + my_id
    #print(srcauthurl)
    response2 = requests.get(srcauthurl, headers=headers, data=payload, verify=False)
    json_response2 = response2.json()
    initial_result = json_response2['response']
    #print(initial_result)
    final_result = json.dumps(initial_result)
    #print("this is separation")
    response_post = requests.request("POST", dsturl, headers=headers, data=final_result, verify=False)
    print(response_post)
    i += 1






