from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    operator = input().split()
    if len(operator) == 1:
        if operator[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif operator[0] == "size":
            print(len(queue))
        elif operator[0] == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif operator[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        else:
            if queue:
                print(queue[-1])
            else:
                print(-1)        
    else:
        queue.append(operator[1])
        
