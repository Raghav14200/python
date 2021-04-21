s=set()

#set does not allow duplicate
s.add(1)
s.add(2)
s.add(3)
s.add(2)

print(s)

list=[1,2,3,4,5,6,4]
s_from_list=set(list)

#union
s1=s.union(s_from_list)
print(s1)

#intersection
s2=s.intersection(s_from_list)
print(s2)

s.remove(2)
print(s)

