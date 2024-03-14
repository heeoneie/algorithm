import sys

input = sys.stdin.readline
n,m = map(int, input().split())
people = {}
res = []
for _ in range(n):
    person = input().strip()
    people[person] = False
    
for _ in range(m):
    person = input().strip()
    if person in people:
        people[person] = True
    else:
        people[person] = False

for person in people:
    if people.get(person):
        res.append(person)

res = sorted(res)
print(len(res))
for i in res:
    print(i)