
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


cursor = connection.cursor(dictionary=True)
sql_update_query = "Update temp set expired = %s "
input_data = ("yes",)
cursor.execute(sql_update_query, input_data)
connection.commit()







cursor2 = connection.cursor(dictionary=True)
sql_update_query2 = "Update authz set expired = %s "
input_data2 = ("yes",)
cursor2.execute(sql_update_query2, input_data2)
connection.commit()
