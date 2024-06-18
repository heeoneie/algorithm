import sys

n = int(sys.stdin.readline())
start, end = 1,1
sum_val = 1
cnt = 1

while end < n:
    if sum_val < n:
        end += 1
        sum_val += end
    elif sum_val > n:
        sum_val -= start
        start += 1
    else:
        cnt += 1
        sum_val -= start
        start += 1
        
print(cnt)