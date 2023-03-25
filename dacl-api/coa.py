import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url = "https://ise32.taimoorlab.local/admin/API/mnt/CoA/Reauth/ise-proxy2/00:50:56:8D:66:BC/1"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
