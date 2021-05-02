name=input("Enter your Name ")
usn=input("Enter your usn ")
phone=input("Enter your phone no ")

print(f"hi {name} is this your usn : {usn} and your phone no : {phone}")

msg=''' This is a message from {name} usn {usn} to the C.R'''

print(msg.format(name=name ,usn=usn))
