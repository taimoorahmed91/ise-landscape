import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url = "https://ise32.taimoorlab.local:9060/ers/config/authorizationprofile"

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
