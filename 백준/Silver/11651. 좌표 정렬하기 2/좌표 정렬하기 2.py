import sys

input = sys.stdin.readline
n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

coords.sort()
coords.sort(key=lambda y:y[1])

for coord in coords:
    print(coord[0], coord[1])