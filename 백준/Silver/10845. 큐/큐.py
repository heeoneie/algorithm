from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    operator = input().split()
    if len(operator) == 1:
        if operator[0] == "pop":
            print(queue.popleft() if queue else -1)
        elif operator[0] == "size":
            print(len(queue))
        elif operator[0] == "empty":
            print(0 if queue else 1)
        elif operator[0] == "front":
            print(queue[0] if queue else -1)
        else:
            print(queue[-1] if queue else -1)
    else:
        queue.append(int(operator[1]))