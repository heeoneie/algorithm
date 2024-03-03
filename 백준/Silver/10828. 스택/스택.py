import sys

input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    operator = input().split()
    if len(operator) == 1:
        if operator[0] == "pop":
            print(stack.pop() if stack else -1)
        elif operator[0] == "size":
            print(len(stack))
        elif operator[0] == "empty":
            print(0 if stack else 1)
        else:
            print(stack[-1] if stack else -1)
    else:
        stack.append(int(operator[1]))