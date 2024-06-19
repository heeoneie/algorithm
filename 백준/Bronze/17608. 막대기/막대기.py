import sys

input = sys.stdin.readline
n = int(input())
stack = [int(input()) for _ in range(n)]
cnt = 1
temp = stack.pop()

for _ in range(n-1):
    next_value = stack.pop()
    if next_value > temp:
        cnt += 1
        temp = next_value
        
print(cnt)
