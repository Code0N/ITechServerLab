import requests

files = {'file': open('FR.exe', 'rb')}

r = requests.post('http://localhost:8080/', files=files)
print(r.text)
