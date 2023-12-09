x = int(input())
n = int(input())
temp = 0

for _ in range(n):
    a, b = map(int, input().split())
    temp = temp + a * b
if temp == x:
    print("Yes")
else:
    print("No")
