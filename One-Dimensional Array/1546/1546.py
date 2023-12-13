m = int(input())
score = list(map(int, input().split()))
high = max(score)
aver = 0
for i in range(m):
    aver = aver + score[i]/high*100
print(aver/m)
