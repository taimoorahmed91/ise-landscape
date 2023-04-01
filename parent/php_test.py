

import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



connection = mysql.connector.connect(host='odbc.taimoorlab.local',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')



cursor = connection.cursor(dictionary=True)
sql_insert_query = "INSERT INTO php_call (descrio) VALUES (%s)"
val = ("samepl_data",)
cursor.execute(sql_insert_query, val)
connection.commit()
