import sys

input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
schedule.sort(key=lambda x : (x[1],x[0]))

cnt = 1
end_time = schedule[0][1]
for i in range(1,n):
    if schedule[i][0] >= end_time:
        cnt += 1
        end_time = schedule[i][1]
        
print(cnt)