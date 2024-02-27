import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    stack = []
    VPS = input()
    for i in VPS:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack: # 0이 아니면 TRUE
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")