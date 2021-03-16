import re
sum=0
fhand=open("t.txt")
for line in fhand:
             y=re.findall('[0-9]+',line)
             for i in y:
                  sum+=int(i)
print(sum)