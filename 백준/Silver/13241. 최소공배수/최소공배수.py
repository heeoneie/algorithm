import sys
def find_gcd(a,b):
    if a%b == 0:
        return b
    return find_gcd(b,a%b)
a,b = map(int, sys.stdin.readline().split())
gcd = find_gcd(a,b)

print(gcd*a//gcd*b//gcd)