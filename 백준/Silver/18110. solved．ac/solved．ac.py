import sys
from collections import deque

def round(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)
    
input = sys.stdin.readline
n = int(input())
m = round(n*0.15)
levels = sorted(list(int(input()) for _ in range(n)))
levels = deque(levels)

if n != 0:
    for _ in range(m):
        levels.popleft()
    for _ in range(m):
        levels.pop()
    
    print(round(sum(levels)/len(levels)))
else:
    print(0)