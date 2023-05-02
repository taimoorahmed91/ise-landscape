import urllib3
import requests
import sys
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#will accept policy name


srcid = sys.argv[1]




connection = mysql.connector.connect(host='127.0.0.1',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')

cursor = connection.cursor(dictionary=True)
sql_update_query = """Update policyset set srcid = %s where id = 5"""
input_data = (srcid,)
cursor.execute(sql_update_query, input_data)
connection.commit()
