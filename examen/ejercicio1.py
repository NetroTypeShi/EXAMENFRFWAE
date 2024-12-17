import requests
import re
url = "http://192.168.60.211:8080"
response = requests.get(url)
print(response.text)