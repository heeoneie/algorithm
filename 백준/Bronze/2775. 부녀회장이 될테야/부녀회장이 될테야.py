import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    floor = int(input())
    unit = int(input())
    inhabitant = [i for i in range(1,unit+1)]
    for _ in range(floor):
        for i in range(1,unit):
            inhabitant[i] += inhabitant[i-1]
    print(inhabitant[-1])