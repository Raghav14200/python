array=[1,2,3,4,5,"raghu","google","youtube"]
array.append("Whatsapp")
array.append("Twitter")
for i in array:
    print(i)

array.remove("google")
for i in array:
    print(i)

print(array[0])
print(array[4])
print(len(array))
print(type(array))
