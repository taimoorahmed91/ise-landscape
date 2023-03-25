

import json
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = "https://ise32.taimoorlab.local/ers/config/adminuser"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
user = 'admin'
pw = 'C1sc0123@'


login_response = requests.post(url, auth=(user, pw), verify=False)
print(login_response)
