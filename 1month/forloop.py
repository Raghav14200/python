name=['Raghavendra','Yashu','Pratheek','Sudeep','Suman','Punith']

for i in name:
    print(i)


alphabets=[['a',1],['b',2],['c',3],['d',4],['e',5]]

for alphabet,no in alphabets:
    print(alphabet,no)

items=['int','float',5,7,8,2,'hello',15]

for i in items:
    if str(i).isnumeric() and i>6:
        print(i)
