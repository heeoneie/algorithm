import sys

input = sys.stdin.readline
n,m = map(int, input().split())
S = [input() for _ in range(n)]
words = [input() for _ in range(m)]
cnt = {}
res = 0

for s in S:
    cnt[s] = 1

for word in words:
    if cnt.get(word) == 1:
        res += 1
        
print(res)
    