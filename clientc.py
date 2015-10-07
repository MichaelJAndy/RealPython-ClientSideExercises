import requests

__author__ = 'mandreacchio'

url = "http://httpbin.org/post"
data = {'fname': "Michael", 'lname': 'Andy'}

r = requests.post(url, data=data)

print(r)

