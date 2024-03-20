import sys

input = sys.stdin.readline
n = int(input())
dancers = {"ChongChong"}

for _ in range(n):
    people = input().rstrip().split()
    
    if people[0] in dancers:
        dancers.add(people[1])
    if people[1] in dancers:
        dancers.add(people[0])

print(len(dancers))