
#list is mutable
count=[1,6,3,7,5]
stocks=["april","blue","rag",56,78]

count.append(16)
count.append(18)

count.insert(2,54)

for i in count:
    print(i,end=' ')

print("")

for i in stocks:
    print(i,end=" ")

print(" ")

#array.sort() changes the original array.
count.sort()

for i in count:
    print(i,end=' ')

print(" ")

#array.reverse() reverses the original array.
count.reverse()
for i in count:
    print(i,end=' ')

print(" ")

#tuple is immutable
tuple=(1,2,3)

print(tuple)

#swaping in python
a=8
b=5
a,b=b,a
print(a,b)

