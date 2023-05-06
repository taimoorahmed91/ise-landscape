import urllib3
import requests
import sys
import json
import mysql.connector
import contextlib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#will accept isename and policysetid


isename = sys.argv[1]
policysetid = sys.argv[2]
name = sys.argv[3]



connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')






authentication = "authentication"




firsthalfurl = "https://"
secondhalfurl = "/api/v1/policy/network-access/policy-set"

url = firsthalfurl + isename + secondhalfurl + "/" + policysetid

#print(url)




payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(url, headers=headers, data=payload, verify=False)
result =(response.text)
#print(result)


json_response = response.json()


filename = "/root/ise-landscape/policyset/policy-sets/"  + policysetid 


with open(filename, "w") as o:
    with contextlib.redirect_stdout(o):
        print(result)

