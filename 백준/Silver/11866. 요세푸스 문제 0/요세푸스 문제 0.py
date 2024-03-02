import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])
res = []

while len(queue) != 0:
    for _ in range(k-1):
        queue.append(queue.popleft())
    res.append(str(queue.popleft()))
    
print('<'+', '.join(res)+'>')