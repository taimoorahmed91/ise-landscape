import pymysql
import pyrad
from pyrad import dictionary, packet, client
import hashlib

# Database connection details
db_host = 'localhost'
db_username = 'root'
db_password = 'C1sc0123@'
db_name = 'mise'

# Attribute names from the dictionary
ATTRIBUTE_USER_NAME = "User-Name"
ATTRIBUTE_NAS_IP_ADDRESS = "NAS-IP-Address"
ATTRIBUTE_USER_PASSWORD = "User-Password"

def encrypt_password(password, secret):
    # Pad the password to a multiple of 16 bytes
    password = password.encode("utf-8")
    pad_len = 16 - (len(password) % 16)
    password += bytes([pad_len]) * pad_len

    # Use MD5 encryption for the password
    md5 = hashlib.md5(secret.encode() + password)
    return md5.digest()

def send_radius_request():
    # Connect to the database and get RADIUS server details
    with pymysql.connect(host=db_host, user=db_username, password=db_password, db=db_name) as db:
        with db.cursor() as cursor:
            sql = "SELECT hostname, radiuskey FROM radius WHERE active = 'yes'"
            cursor.execute(sql)
            result = cursor.fetchone()

    if result:
        radius_hostname, radius_secret = result
        print("RADIUS Secret:", radius_secret)

        # Create RADIUS client
        radius_client = client.Client(server=radius_hostname, secret=radius_secret.encode(), dict=dictionary.Dictionary("dictionary"))

        # Create RADIUS request packet
        req = radius_client.CreateAuthPacket(code=packet.AccessRequest)
        req[ATTRIBUTE_USER_NAME] = "sample"

        # Add NAS-IP-Address attribute
        nas_ip_address = "172.17.30.213"
        req.AddAttribute(ATTRIBUTE_NAS_IP_ADDRESS, nas_ip_address)

        # Add User-Password attribute (encrypted)
        user_password = "cisco"  # Replace this with the actual user password
        encrypted_password = encrypt_password(user_password, radius_secret)
        req.AddAttribute(ATTRIBUTE_USER_PASSWORD, encrypted_password)

        # Send RADIUS request
        try:
            reply = radius_client.SendPacket(req)
            print("Received RADIUS reply")
            print(reply)
        except pyrad.client.TimeoutError:
            print("RADIUS request timed out")
        except pyrad.client.NoResponse:
            print("No response received from RADIUS server")

        print("Password:", user_password)

if __name__ == "__main__":
    send_radius_request()

