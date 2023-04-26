
import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')
sql_select_Query = "select * from ap where expired = 'no'"

cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


ap = sys.argv[1]


#print(dacl)


url = "https://ise32.taimoorlab.local/ers/config/allowedprotocols/"

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
    if value['name'] == ap:
        my_id=(value['id'])


#print(my_id)




# start push from here


newurl = url + my_id

response2 = requests.request("GET", newurl, headers=headers, data=payload, verify=False)

result =(response2.text)

#print(result)




post_url ='https://ise-proxy2.taimoorlab.local/ers/config/allowedprotocols'


response_post = requests.request("POST", post_url, headers=headers, data=result, verify=False)
print(response_post)


# update code to db


## updates to be pushed to db are from here


http_code = str(response_post)
http_code = http_code[:-1]
http_code = http_code[1:]
print(http_code)







cursor = connection.cursor(dictionary=True)
sql_update_query = """Update ap set code_post = %s where ap = %s"""
input_data = (http_code, ap)
cursor.execute(sql_update_query, input_data)
connection.commit()
