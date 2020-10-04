import urllib.request,urllib.parse,urllib.error
import json
x=input("Enter Url")
fhand=urllib.request.urlopen(x).read().decode()
y=json.loads(fhand)
#print(y["comments"])
sum=0
for i in y["comments"]:
        sum+=i["count"]
print(sum)           