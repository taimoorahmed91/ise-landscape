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


sql_select_Query = "select * from odbc"
cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


mac = sys.argv[1]


#print(dacl)

initial_url = "https://ise32.taimoorlab.local/admin/API/mnt/CoA/Reauth/ise-proxy2/"
code = "/1"

url = initial_url + mac + code

#print(url)



payload={}
headers = {
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(url, headers=headers, data=payload, verify=False)



#print(response)



coa_code = str(response)
coa_code = coa_code[:-1]
coa_code = coa_code[1:]
print(coa_code)




## updates to be pushed to db are from here


cursor = connection.cursor(dictionary=True)
sql_update_query = """Update odbc set coa_code = %s where mac = %s"""
input_data = (coa_code, mac)
cursor.execute(sql_update_query, input_data)
connection.commit()
