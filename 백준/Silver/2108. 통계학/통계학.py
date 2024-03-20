import sys

input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
cnt = {}

for i in num:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

maxDict = max(cnt.values())
res = []

for i in cnt:
    if maxDict == cnt[i]:
        res.append(i)

print(round(sum(num)/n))
print(num[n//2])
print(res[1] if len(res) > 1 else res[0])
print(max(num) - min(num))