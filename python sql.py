import sqlite3
import xml.etree.ElementTree as et
conn=sqlite3.connect("db2.sqlite")
cur=conn.cursor()
cur.executescript('''
DROP table IF EXISTS Artist;
DROP table IF EXISTS Genre;
DROP table IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT 
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT 
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT 
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

def lookup(d,key):
	found=False
	for t in d:
		if found:
			return t.text
		if t.tag== 'key' and t.text==key:
			found=True
	return None

fhand=open("Library.xml").read()
data=et.fromstring(fhand)
data1=data.findall('dict/dict/dict')
for row in data1:
	name1=lookup(row,'Name')
	artist1=lookup(row,'Artist')
	album1=lookup(row,'Album')
	genre1=lookup(row,'Genre')
	print(name1,artist1,album1)
	if name1 is None or artist1 is None or album1 is None or genre1 is None: 
        	continue

	cur.execute('''INSERT INTO Artist (name) VALUES ( ? )''', ( artist1, ) )
	cur.execute('INSERT INTO Genre (name) VALUES ( ? )', ( genre1, ) )
	cur.execute('select id from Artist where name=?',(artist1,))
	artist_id=cur.fetchone()[0]
	cur.execute('select id from Genre where name=?',(genre1,))
	genre_id=cur.fetchone()[0]
	cur.execute('INSERT INTO Album (title,artist_id) VALUES ( ?,? )', ( album1,  artist_id) )
	cur.execute('select id from Album where title=?',(album1,))
	album_id=cur.fetchone()[0]
	cur.execute('INSERT INTO Track (title,album_id,genre_id) VALUES ( ?,?,? )', ( name1,album_id,genre_id ) )
	conn.commit()

conn.close()	
	
	

