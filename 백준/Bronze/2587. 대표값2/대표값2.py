import sys

numbers = [int(sys.stdin.readline()) for _ in range(5)]

for i in range(len(numbers)-1,0,-1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(sum(numbers)//5)
print(numbers[2])