import sys
input = sys.stdin.readline

t = int(input())

def isPrimeNum(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for _ in range(t):
    n = int(input())
    while True:
        if isPrimeNum(n):
            print(n)
            break
        else:
            n += 1
    