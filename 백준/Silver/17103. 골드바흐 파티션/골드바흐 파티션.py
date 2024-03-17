import sys

input = sys.stdin.readline
primeNum = [False, False] + [True] * 999999
for i in range(2,len(primeNum)):
    if not primeNum[i]:
        continue
    for j in range(i+i,len(primeNum),i):
        primeNum[j] = False

t = int(input().rstrip())
for _ in range(t):
    cnt = 0
    n = int(input().rstrip())
    for i in range(2,n//2+1):
        if primeNum[i] and primeNum[n-i]:
            cnt += 1
    print(cnt)
