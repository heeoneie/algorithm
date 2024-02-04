import sys
input = sys.stdin.readline().rstrip

n = input()
res = []

for i in range(len(n)):
    res.append(int(n[i]))
    
res.sort(reverse=True)
print(*res, sep="")
