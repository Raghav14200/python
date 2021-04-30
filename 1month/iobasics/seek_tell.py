file=open("sample2.txt","r")

print(file.tell())#prints the pointer location
print(file.readline())
print(file.tell())

file.seek(10)
print(file.readline())
file.close()

