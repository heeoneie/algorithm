from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
deq = deque()

for _ in range(n):
    operator = input().split()
    if len(operator) == 1:
        if operator[0] == "pop_front":
            print(deq.popleft() if deq else -1)
        elif operator[0] == "pop_back":
            print(deq.pop() if deq else -1)
        elif operator[0] == "size":
            print(len(deq))
        elif operator[0] == "empty":
            print(0 if deq else 1)
        elif operator[0] == "front":
            print(deq[0] if deq else -1)
        else:
            print(deq[-1] if deq else -1)
    else:
        x = int(operator[1])
        if operator[0] == "push_front":
            deq.appendleft(x)
        else:
            deq.append(x)