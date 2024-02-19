import sys, math
input = sys.stdin.readline

n = int(input())
street = [int(input()) for _ in range(n)]
gap = []

for i in range(n-1):
    gap.append(street[i+1]-street[i])

gcd = gap[0]
for j in range(1,len(gap)):
    gcd = math.gcd(gcd,gap[j])

res = 0
for k in gap:
    res += k // gcd -1

print(res)
