import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queuestack = list(map(int, input().split()))
element = list(map(int, input().split()))
m = int(input())
inElement = list(map(int, input().split()))
res = deque()

for i in range(n):
    if queuestack[i] == 0:
        res.append(element[i])

for i in range(m):
    res.appendleft(inElement[i])
    print(res.pop(),end=' ')