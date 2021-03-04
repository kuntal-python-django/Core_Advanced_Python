import requests
import json 

website_path = input("Enter Website Name : \n")
res = requests.get(website_path)
print(res.status_code)
print(res.headers['content-type'])
print(res.encoding)

data = res.json()
print(data)
data = json.dumps(data)
f= open("Web_Response.txt","w+")
f.write(data)
f.close()