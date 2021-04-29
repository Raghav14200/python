"""
"r" -> open file for reading
"w" -> open file for writing
"x" -> creates file if not exists.
"a" -> Add more content to a file.
"t" -> text mode.
"b" -> binary mode.
"+" -> read and write.
"""

#read file named sample.txt
file=open("sample.txt")
print(file.readlines())
file.close()

file=open("sample.txt")
content=file.read()
print(content)
file.close()

#write into file.
file=open("sample2.txt","w")
file.write("I am writing into file using python console")
file.close()

#Append into file.
file=open("sample.txt","a")
length=file.write("I have appended in sample file")
print(length)#returns the length that has been appended.
file.close()

file=open("sample2.txt","r")
print(file.read())
file.close()

#handle read and write both
file=open("sample2.txt","r+")
print(file.read())
file.write("Thanks for your corporation")
print(file.read())
file.close()







