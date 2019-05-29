# the file will be used to request the file from the server
import requests
url = 'http://localhost:5000/api'
r  = requests.post(url,json= {'exp': 11.2,})
print(r.json())
