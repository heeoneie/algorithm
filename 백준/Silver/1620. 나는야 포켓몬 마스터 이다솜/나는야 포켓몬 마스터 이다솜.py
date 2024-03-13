import sys

input = sys.stdin.readline
n,m = map(int, input().split())
poketDict = {}

for i in range(1,n+1):
    poketmonster = input().rstrip()
    poketDict[poketmonster] = i
    poketDict[i] = poketmonster

for _ in range(m):
    operation = input().rstrip()
    if operation.isdigit():
        print(poketDict[int(operation)])
    else:
        print(poketDict[operation])