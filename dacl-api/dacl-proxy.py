import os
import urllib3
import requests

# Disabling SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setting environment variables for the proxy
os.environ['HTTP_PROXY'] = 'https://prod.radkit-cloud.cisco.com/pac?port=4000'
os.environ['HTTPS_PROXY'] = 'https://prod.radkit-cloud.cisco.com/pac?port=4000'

# API Endpoint
url = "https://lab1.982c-g2aw-75l2.proxy"

# Request payload and headers
payload = {}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}

# Sending the request
response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)

