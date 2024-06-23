import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
num = [i for i in range(1,n+1)]
num = deque(num)
res = []

while num:
    num.rotate(-(k-1))
    res.append(num.popleft())
    
print("<",", ".join(map(str, res)),">", sep="")
