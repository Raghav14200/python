import sqlite3
import re
import urllib.request,urllib.parse,urllib.error
conn=sqlite3.connect('database1.sqlite')
cur=conn.cursor()
cur.execute('Drop Table if exists Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
fhand=open('mbox.txt')
for line in fhand:
	if line.startswith("From: "):
			y=line.split(" ")
			z=re.findall('\S+@(\S+)+',y[1])
			print(z[0])

			cur.execute('SELECT count FROM Counts WHERE org = ? ', (z[0],))
			row=cur.fetchone()
			if row is None:
                		cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (z[0],))
			else:
                		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(z[0],))
conn.commit()

for row in cur.execute('SELECT count FROM Counts'):
	print(row[0]) 
cur.close()

