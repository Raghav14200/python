import time

i=0
while(i<10):
	i+=1
	print(time.time())
	print(time.localtime(time.time()))
	print(time.asctime(time.localtime(time.time())))
	print()
	print("**************")
	print()

