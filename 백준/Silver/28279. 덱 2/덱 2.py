from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
deq = deque()

for _ in range(n):
    operator = input().split()
    if len(operator) == 1:
        if operator[0] == '3':
            print(deq.popleft() if deq else -1)
        elif operator[0] == '4':
            print(deq.pop() if deq else -1)
        elif operator[0] == '5':
            print(len(deq))
        elif operator[0] == '6':
            print(0 if deq else 1)
        elif operator[0] == '7':
            print(deq[0] if deq else -1)
        else:
            print(deq[-1] if deq else -1)
    else:
        if operator[0] == '1':
            deq.appendleft(int(operator[1]))
        else:
            deq.append(int(operator[1]))