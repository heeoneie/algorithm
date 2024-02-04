import sys
input = sys.stdin.readline

n = int(input())
numbers = [0] * (10000+1)

for _ in range(n):
    numbers[int(input())] += 1
    
for i in range(len(numbers)):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)