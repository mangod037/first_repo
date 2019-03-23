#연습문제 (리스트 내장함수)
lst = ['Life', 'is', 'too', 'short']
str = " ".join(lst)
print(str)

#연습문제 (if)
a = "Life is too short, you need python"
if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
    #shirt가 프린트 됨

#연습문제 (while문 별찍기)
count = 1
while count < 5:
    print('*'*count)
    count += 1

#연습문제 (모음찾기)
str1 = 'mutzangesazachurum'
count1 = 0
for i in str1:
    if i in 'aeiou':
        count1 += 1
print(count1)

#과제 1 (while)
#1-1
sum = 0
num = 0
while num < 1000:
    num += 1
    if num % 3 != 0:
        continue
    sum += num
print(sum)

#1-2
count2 = 10
while count2 > 0:
    print('*'*count2)
    count2 -= 1

#1-3
lst2 = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
count3 = -1
sum2 = 0
while count3 < len(lst2)-1:
    count3 += 1
    if lst2[count3] < 50:
        continue
    sum2 += lst2[count3]
print(sum2)

#과제 2 (for)
#2-1
for i in range(1,101):
    print(i)

#2-2
lst3 = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum3 = 0
for i in lst3:
    sum3 += i
print(sum3/len(lst3))

#2-3
numbers = [1,2,3,4,5,6,7,8,9]
result = []
for i in numbers:
    if i % 2 == 1:
        result.append(i*2)
print(result)
