import requests

r=requests.get("http://httpbin.org/json")
print(r)
jsonfile=r.json()
print(jsonfile)