import urllib3
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url = "https://lab1.982c-g2aw-75l2.proxy/ers/config/downloadableacl"

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)
