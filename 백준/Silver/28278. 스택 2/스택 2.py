import sys
input = sys.stdin.readline
n = int(input())
stack = []

for _ in range(n):
    operator = input().split()
    if len(operator) == 1:
        if operator[0] == '2':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif operator[0] == '3':
            print(len(stack))
        elif operator[0] == '4':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
    else:
        stack.append(int(operator[1]))