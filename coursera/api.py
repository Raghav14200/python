import urllib.request,urllib.parse,urllib.error
import json
url=input("Enter url")
city={}
city["address"]='Boston University'
city["key"]=42
url=url+urllib.parse.urlencode(city)
fhand=urllib.request.urlopen(url).read().decode()
x=json.loads(fhand)
print(x["results"][0]["place_id"])
