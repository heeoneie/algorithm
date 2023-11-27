N = int(input())
a = list(map(int,input().split()))
v = int(input())
temp = 0

for i in range(N):
    if a[i] == v:
        temp = temp + 1
print(temp)
