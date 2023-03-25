import urllib3
import requests
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



url = "https://ise32.taimoorlab.local:9060/ers/config/downloadableacl/"

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(url, headers=headers, data=payload, verify=False)

json_response = response.json()


#print(json.dumps(json_response))

for value in json_response['SearchResult']['resources']:
    if value['name'] == 'dACL_sample':
        my_id=(value['id'])


print(my_id)

print(url)


newurl = url + my_id

response2 = requests.request("GET", newurl, headers=headers, data=payload, verify=False)

print(response2.text)
