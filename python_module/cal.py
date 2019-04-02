from mod import *

print("python cal.py\nMenu\n---------")
print("1: add\n2: sub\n3: multiply\n4: divide\n5: stop")

while True:
    a = input("input number: ")
    if a == '1':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(add(num1, num2))
    if a == '2':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(sub(num1, num2))
    if a == '3':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(mul(num1, num2))
    if a == '4':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(div(num1, num2))
    if a == '5':
        break