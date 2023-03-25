from pprint import pprint
import urllib3
import requests
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url = "https://ise32.taimoorlab.local:9060/ers/config/authorizationprofile/name/ipsk_authz"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic dGFpYWhtZWQ6QzFzYzAxMjNA',
}

response = requests.get(url, headers=headers, data=payload, verify=False).json()

pprint(response)

