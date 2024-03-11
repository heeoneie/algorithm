import sys

input = sys.stdin.readline
n = int(input())
workers = {}

for _ in range(n):
    worker, state = input().split()
    if state == "enter":
        workers[worker] = True
    else:
        del workers[worker]
        
workers = sorted(workers.keys(), reverse=True)

for worker in workers:
    print(worker)