import sys
n,k = map(int, sys.stdin.readline().split())

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def collect(n,k):
    return factorial(n) // factorial(n-k) // factorial(k)

print(collect(n,k))