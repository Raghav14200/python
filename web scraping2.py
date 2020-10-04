import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
count=7
position=18
link='http://py4e-data.dr-chuck.net/known_by_Nicole.html'
while(count):
            count-=1
            fhand=urllib.request.urlopen(link).read()
            f2=BeautifulSoup(fhand,'html.parser')
            l=f2('a')
            link=l[position-1].get('href',None)
print(link)