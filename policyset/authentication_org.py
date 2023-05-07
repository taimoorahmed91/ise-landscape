import urllib3
import requests
import sys
import json
import mysql.connector
import contextlib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#will accept isename and policysetid and policysetname


isename = sys.argv[1]
policysetid = sys.argv[2]
policysetname = sys.argv[3]

connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')



authentication = "/authentication"




firsthalfurl = "https://"
secondhalfurl = "/api/v1/policy/network-access/policy-set/"

url = firsthalfurl + isename + secondhalfurl + policysetid + authentication 

#print(url)




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


length = 100

i = 0

initial_filename = "/root/ise-landscape/policyset/authentications/"  

while i < length:
    my_id = json_response['response'][i]['rule']['id']
    #print(my_id)
    my_name = json_response['response'][i]['rule']['name']
    #print(my_name)
    srcauthurl = url + "/" + my_id
    #print(srcauthurl)
    response2 = requests.get(srcauthurl, headers=headers, data=payload, verify=False)
    json_response2 = response2.json()
    initial_result = json_response2['response']
    #print(initial_result)
    final_result = json.dumps(initial_result)
    #print(final_result)
    filename = initial_filename + my_id
    with open(filename, "w") as o:
            with contextlib.redirect_stdout(o):
                    print(final_result)
    response_post = str(response2)
    response_post = response_post[:-1]
    response_post = response_post[1:]
    #print(response_post)
    




    cursor = connection.cursor(dictionary=True)
    sql_insert_query = "INSERT INTO authentications (authenticationname,authenticationid	, fetchedfrom,sourceise, code) VALUES ( %s, %s, %s, %s, %s)"
    val = (my_name,my_id,policysetname,isename,response_post)
    cursor.execute(sql_insert_query, val)
    connection.commit()
    i += 1



