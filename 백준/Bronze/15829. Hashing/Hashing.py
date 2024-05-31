import sys

input = sys.stdin.readline
n = int(input())
word = input().rstrip()
ans = 0

for i in range(n):
    ans += (ord(word[i])-96) * (31**i)
print(ans % 1234567891)