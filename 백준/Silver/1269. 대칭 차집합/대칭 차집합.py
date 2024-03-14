import sys

input = sys.stdin.readline
n,m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
temp = a - b
temp2 = b - a
res = set(temp|temp2)
print(len(res))