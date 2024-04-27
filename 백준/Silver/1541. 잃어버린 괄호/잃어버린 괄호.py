import sys

cal = sys.stdin.readline().split('-')
numbers = []
for i in cal:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum += int(j)
    numbers.append(sum)

number = numbers[0]
for i in range(1,len(numbers)):
    number -= numbers[i]

print(number)