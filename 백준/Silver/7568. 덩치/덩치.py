import sys

input = sys.stdin.readline
n = int(input())
students = []

for _ in range(n):
    weight, tall = map(int, input().split())
    students.append([weight, tall])

for i in students:
    rank = 1
    for j in students:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
