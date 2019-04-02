from mod import *

print("python cal.py\nMenu\n---------")
print("1: add\n2: sub\n3: multiply\n4: divide\n5: stop")

while True:
    a = input("input number: ")
    if a == '1':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(add(num1, num2))
    elif a == '2':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(sub(num1, num2))
    elif a == '3':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        print(mul(num1, num2))
    elif a == '4':
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
        if num2 == 0:
            print("0으로는 나눌 수 없습니다")
        else:
            print(div(num1, num2))
    elif a == '5':
        print("프로그램을 끝냅니다")
        break
    else:
        print("숫자를 제대로 입력하세요")