print("Enter num 1")
num1 = input()

print("Enter num 2")
num2 = input()

try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is very important")

