import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
ans = []
for i in range(m,n+1):
    sqrt_i = int(i**0.5)
    if sqrt_i**2 == i:
        ans.append(i)

if len(ans):
    print(sum(ans), ans[0])
else:
    print(-1)