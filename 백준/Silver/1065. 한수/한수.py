import sys

input = sys.stdin.readline
n = int(input())
cnt = 0
# 100미만은 비교대상이 없어 전부 한수디
# 100이상부터는 공차가 같으면 cnt += 1
for i in range(1,n+1):
    if i < 100:
        cnt += 1
    else:
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            cnt += 1        
print(cnt)
        