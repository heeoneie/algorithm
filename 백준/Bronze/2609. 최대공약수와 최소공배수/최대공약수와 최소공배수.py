a, b = map(int, input().split())
def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b, a%b)
    
max = gcd(a,b)
min = max * (a//max) * (b//max)

print(max)
print(min)