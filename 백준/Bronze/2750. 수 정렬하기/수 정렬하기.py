n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

for i in range(len(numbers)-1,0,-1):
    for j in range(i):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for i in range(len(numbers)):            
    print(numbers[i])