import sys
n,m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(len(card)):
    for j in range(i+1,len(card)):
        for k in range(j+1,len(card)):
            blackJack = card[i]+card[j]+card[k]
            if blackJack <= m:
                res.append(blackJack)
print(max(res))