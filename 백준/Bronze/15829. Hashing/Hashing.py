import sys

input = sys.stdin.readline
n = int(input())
word = input().rstrip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = 0

for i in range(n):
    idx = alphabet.index(word[i]) + 1
    ans += idx * 31**i

print(ans)