

import json
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ise32.taimoorlab.local:9060/ers/config/adminuser"
headers = {'Content-Type': 'application/json' ,'Accept': 'application/json', 'Authorization':'taiahmed:C1sc0123@'}
user = 'taiahmed'
pw = 'C1sc0123@'
payload={}


response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)


