import urllib3
import requests
import sys
import json
import mysql.connector
import contextlib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


fqdn = sys.argv[1]


connection = mysql.connector.connect(host='127.0.0.1',
                                     database='mise',
                                     user='root',
                                     password='C1sc0123@')




url1 = "https://"
url2 = "/ers/config/downloadableacl"

url = url1 + fqdn + url2


initial_webfilename = "/var/www/html/landscape/configs/authz/"

payload={}
headers = {
          'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Basic YWRtaW46QzFzYzAxMjNA',
}
response = requests.get(url, headers=headers, data=payload, verify=False)
result =(response.text)
#print(result)

json_response = response.json()
#print(json_response)


length = 1000

i = 0

while i < length:
    my_id = json_response['SearchResult']['resources'][i]['id']
    #print(my_id)
    my_name = json_response['SearchResult']['resources'][i]['name']
    #print(my_name)
    srcauthurl = url + "/" + my_id
    #print(srcauthurl)
    response2 = requests.get(srcauthurl, headers=headers, data=payload, verify=False)
    text_result = (response2.text)
    filename_web = initial_webfilename + my_id
    with open(filename_web, "w") as o:
        with contextlib.redirect_stdout(o):
            print(text_result)

    response_post = str(response2)
    response_post = response_post[:-1]
    response_post = response_post[1:]
    #print(response_post)
    cursor = connection.cursor(dictionary=True)
    sql_insert_query = "INSERT INTO authz (authz,authzid,isename,get_code) VALUES (%s, %s, %s, %s)"
    val = (my_name,my_id,fqdn,response_post)
    cursor.execute(sql_insert_query, val)
    connection.commit()




    i += 1
