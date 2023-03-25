

import urllib.parse
import requests
base_url="https://v6.exchangerate-api.com/v6/Enter your API key here/pair/"
print("Enter the First Currency")
s=input()
print("Enter the Second Currency")
l=input()
value=s+"/"+l
url = base_url+value
print(url)
