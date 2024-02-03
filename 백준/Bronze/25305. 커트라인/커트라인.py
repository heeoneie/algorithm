import sys

n,k = map(int, sys.stdin.readline().rstrip().split())
score = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(score)-1,0,-1):
    for j in range(i):
        if score[j] < score[j+1]:
            score[j+1], score[j] = score[j], score[j+1]
print(score[k-1])