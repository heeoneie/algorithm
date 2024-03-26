import sys

def backtracking():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(1,n+1):
        res.append(i)
        backtracking()
        res.pop()
        
n,m = map(int, sys.stdin.readline().rstrip().split())
res = []
backtracking()