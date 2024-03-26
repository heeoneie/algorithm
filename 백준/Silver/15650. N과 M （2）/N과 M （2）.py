import sys

def backtracking(k):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(k,n+1):
        if i not in res:
            res.append(i)
            backtracking(i+1)
            res.pop()

n,m = map(int, sys.stdin.readline().rstrip().split())
res = []
backtracking(1)