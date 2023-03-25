

import requests

url = "http://postman-echo.com/get"

payload={}
headers = {
  'Cookie': 'sails.sid=s%3ATWXDUG2KT9FDgYtMJCYn5VHiCSK56Tzh.E4jvM4jy1VqZ1cKr0TCBxVXxXDAeLKt9RrdBIJrJf1c'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

