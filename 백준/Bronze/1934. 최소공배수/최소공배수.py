import sys
input = sys.stdin.readline

t = int(input())

def findGcd(a,b):
    if a%b == 0:
        return b
    return findGcd(b,a%b)

for _ in range(t):
    a,b = map(int, input().split())
    if b>a:
        temp = 0
        temp = a
        a = b
        b = temp
    gcd = findGcd(a,b)
    print(gcd * a//gcd * b//gcd)