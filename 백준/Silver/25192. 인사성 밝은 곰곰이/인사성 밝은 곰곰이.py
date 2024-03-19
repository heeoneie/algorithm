import sys

input = sys.stdin.readline
n = int(input())
cnt = 0

for _ in range(n):
    member = input().rstrip()
    if member == "ENTER":
        members = {}
    else:
        if member in members:
            continue
        else:
            members[member] = True
            cnt += 1
    
print(cnt)