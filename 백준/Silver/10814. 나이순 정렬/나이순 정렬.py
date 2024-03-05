import sys

input = sys.stdin.readline
n = int(input())

members = [input().split() for _ in range(n)]
for i in range(n):
    members[i][0] = int(members[i][0])
members.sort(key=lambda x:x[0])

for member in members:
    print(member[0], member[1])
