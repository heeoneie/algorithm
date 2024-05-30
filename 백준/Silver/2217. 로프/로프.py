import sys

input = sys.stdin.readline
n = int(input())
ropes = [int(input()) for _ in range(n)]
res = []
ropes.sort()

for rope in ropes:
    res.append(rope*n)
    n -= 1

print(max(res))