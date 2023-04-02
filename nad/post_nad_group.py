
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






url = "https://ise32.taimoorlab.local/ers/config/networkdevicegroup/"

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
        id=(value['id'])
        name=(value['name'])
        desc=(value['description'])


#        print(name)
#        print(desc)

        get_url = url + id
#        print(get_url)


        response2 = requests.get(get_url, headers=headers, data=payload, verify=False)
#        json_response2 = response2.json()
#       print(json_response2)

        result =(response2.text)
#        print(result)




        post_url ='https://ise-proxy2.taimoorlab.local/ers/config/networkdevicegroup/'


        response_post = requests.request("POST", post_url, headers=headers, data=result, verify=False)
        print(response_post)



## Attempting to put as well

        get_url_put ='https://ise-proxy2.taimoorlab.local/ers/config/networkdevicegroup/'

        response_put = requests.get(get_url_put, headers=headers, data=payload, verify=False)
        json_response_put = response_put.json() 

        for value in json_response_put['SearchResult']['resources']:
            if value['name'] == name:
                my_id=(value['id'])
                
#        print(my_id)


        put_url = get_url_put + my_id

        response_put = requests.request("PUT", put_url, headers=headers, data=result, verify=False)
        print(response_put) 

        


        http_code_post = str(response_post)
        http_code_post = http_code_post[:-1]
        http_code_post = http_code_post[1:]
        



        http_code_put = str(response_put)
        http_code_put = http_code_put[:-1]
        http_code_put = http_code_put[1:]







        cursor = connection.cursor(dictionary=True)
        sql_insert_query = "INSERT INTO nadgroup (name, code_post, code_put) VALUES (%s,%s, %s)"
        val = (name, http_code_post, http_code_put)
        cursor.execute(sql_insert_query, val)
        connection.commit()
