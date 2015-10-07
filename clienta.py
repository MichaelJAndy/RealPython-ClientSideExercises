import requests
__author__ = 'mandreacchio'


r = requests.get("http://www.python.org/")

print(r.content)


