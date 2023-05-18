import subprocess
import sys
import urllib3
import requests
import json
import mysql.connector
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




# will accept only fqdn and run all things that were added to queue
# Script to fetch policyset authentication
fqdn = sys.argv[1]
print(fqdn)


connection = mysql.connector.connect(host='127.0.0.1',
                                     database='mise',
                                     user='root',
                                     password='C1sc0123@')




# Process dacl
query_dacl = "SELECT id, daclid FROM dacl WHERE queue = 'yes'"
# Execute your query and retrieve the results
cursor = connection.cursor(dictionary=True)
cursor.execute(query_dacl)
results = cursor.fetchall()

for row in results:
    id = row['id']
    daclid = row['daclid']
    subprocess.run(['sudo', '-S', 'python3', '/root/ise-landscape/mise/post_dacl.py', str(id), fqdn, daclid], check=True)

# Process authz
query_authz = "SELECT id, authzid FROM authz WHERE queue = 'yes'"
# Execute your query and retrieve the results

cursor = connection.cursor(dictionary=True)
cursor.execute(query_authz)
results = cursor.fetchall()

for row in results:
    id = row['id']
    authzid = row['authzid']
    subprocess.run(['sudo', '-S', 'python3', '/root/ise-landscape/mise/post_authz.py', str(id), fqdn, authzid], check=True)

# Process ap
query_ap = "SELECT id, apid FROM ap WHERE queue = 'yes'"
# Execute your query and retrieve the results
cursor = connection.cursor(dictionary=True)
cursor.execute(query_ap)
results = cursor.fetchall()


for row in results:
    id = row['id']
    apid = row['apid']
    subprocess.run(['sudo', '-S', 'python3', '/root/ise-landscape/mise/post_ap.py', str(id), fqdn, apid], check=True)

# Process nad
query_nad = "SELECT id, nadid FROM nad WHERE queue = 'yes'"
# Execute your query and retrieve the results
cursor = connection.cursor(dictionary=True)
cursor.execute(query_nad)
results = cursor.fetchall()

for row in results:
    id = row['id']
    nadid = row['nadid']
    subprocess.run(['sudo', '-S', 'python3', '/root/ise-landscape/mise/post_nad.py', str(id), fqdn, nadid], check=True)

# Process sgt
query_sgt = "SELECT id, sgtid FROM sgt WHERE queue = 'yes'"
# Execute your query and retrieve the results
cursor = connection.cursor(dictionary=True)
cursor.execute(query_sgt)
results = cursor.fetchall()


for row in results:
    id = row['id']
    sgtid = row['sgtid']
    subprocess.run(['sudo', '-S', 'python3', '/root/ise-landscape/mise/post_sgt.py', str(id), fqdn, sgtid], check=True)

