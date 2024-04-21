import sys

def fib(n):
    a=b=1
    for _ in range(3,n+1):
        a, b = b, a+b
    return b

def fibonacci(n):
    return n-2

n = int(sys.stdin.readline())
print(fib(n), fibonacci(n))
