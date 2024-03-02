import sys
input = sys.stdin.readline
n = int(input())
students = list(map(int, input().split()))
stack = []
target = 1

while students:
    if students[0] == target:
        students.pop(0)
        target += 1
    else:
        stack.append(students.pop(0))
        
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break
            
print("Sad" if stack else "Nice")
    