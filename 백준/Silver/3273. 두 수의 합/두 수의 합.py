import sys
input = sys.stdin.readline

n = int(input())
num = sorted(map(int, input().split()))
x = int(input())
start = 0
end = n-1
cnt = 0

while start < end:
    current_sum = num[start] + num[end]
    if  current_sum == x:
        cnt += 1
        start += 1
        end -= 1
    elif current_sum < x:
        start += 1
    else:
        end -= 1
        
print(cnt)