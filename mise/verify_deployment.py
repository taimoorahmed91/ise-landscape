import urllib3
import requests
import sys
import json
import mysql.connector
import contextlib
import datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

fqdn = sys.argv[1]

url1 = "https://"
url2 = "/ers/config/op/systemconfig/iseversion"
url = url1 + fqdn + url2



payload = {}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

json_response = response.json()
resources = json_response['OperationResult']['resultValue'][0]['name']
print(resources)

