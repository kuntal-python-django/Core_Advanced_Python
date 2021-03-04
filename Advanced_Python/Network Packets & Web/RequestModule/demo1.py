import requests

res = requests.get(url="https://indiancybersecuritysolutions.com/python-training-in-kolkata-advance/")
# print(res.status_code)
# print(res.headers)
print(res.text)
