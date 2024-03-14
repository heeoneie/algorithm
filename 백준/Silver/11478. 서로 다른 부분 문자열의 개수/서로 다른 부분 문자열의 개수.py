import sys

s = sys.stdin.readline().rstrip()
res = set()

for i in range(len(s)):
    for j in range(i,len(s)):
        res.add(s[i:j+1])

print(len(res))