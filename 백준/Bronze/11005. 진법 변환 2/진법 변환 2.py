import sys

numList = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n,b = map(int, sys.stdin.readline().rstrip().split())
res = ''
while n:
    res += numList[n%b]
    n //= b

print(res[::-1])