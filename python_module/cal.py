import mod

print("python cal.py\nMenu\n---------")
print("1: add\n2: sub\n3: multiply\n4: divide\n5: stop")

while True:
    a = int(input("input number: "))
    lst = [1,2,3,4,5]
    if a==5:
        print("프로그램을 끝냅니다")
        break
    if a not in lst:
        print("숫자를 제대로 입력하세요")
        continue

    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    b = mod.FourCal(num1, num2)
    
    if a==1:
        print(b.add())
    elif a==2:
        print(b.sub())
    elif a==3:
        print(b.mul())
    elif a==4:
        if num2==0:
            print("0으로는 나눌 수 없습니다")
        else:
            print(b.div())
