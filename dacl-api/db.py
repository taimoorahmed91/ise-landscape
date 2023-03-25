

import urllib3
import requests
import sys
import json
import mysql.connector

connection = mysql.connector.connect(host='odbc.taimoorlab.local',
                                     database='landscape',
                                     user='root',
                                     password='C1sc0123@')
sql_select_Query = "select * from temp where expired = 'yes'"

cursor = connection.cursor(dictionary=True)
cursor.execute(sql_select_Query)
records = cursor.fetchall()


for row in records:
        dacl = row["dacl"]



print(dacl)
