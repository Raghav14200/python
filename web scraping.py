import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
fhand=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_944961.html").read()
f2=BeautifulSoup(fhand,'html.parser')
counts=f2('span');
count=0
for i in counts:
       count+=int(i.contents[0])
print(count)