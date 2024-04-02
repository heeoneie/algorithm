import sys

n = int(sys.stdin.readline())
res = 0
row = [0]*n

def isAttack(x):
    for i in range(x):
        if row[x] == row[i] or abs(x-i) == abs(row[x]-row[i]):
            return False
    return True

def setQueen(x):
    global res
    if x == n:
        res += 1
        return
    
    for i in range(n):
        row[x] = i
        if isAttack(x):
            setQueen(x+1)
            
setQueen(0)
print(res)