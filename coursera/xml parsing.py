import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as et
x=input("Enter URL")
fhand=urllib.request.urlopen(x).read()
y=et.fromstring(fhand)
z=y.findall('comments/comment')
sum=0
for i in z:
      sum+=int(i.find('count').text)
print(sum)