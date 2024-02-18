import sys
input = sys.stdin.readline

def find_gcd(a,b):
    while a%b != 0:
        r = a%b
        a = b
        b = r
    return b
    
a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())

gcd = find_gcd(b1,b2)
lcm = b1*b2//gcd

up = a1*(b2//gcd) + a2*(b1//gcd)
gcd2 = find_gcd(up,lcm)
print(up//gcd2, lcm//gcd2)
