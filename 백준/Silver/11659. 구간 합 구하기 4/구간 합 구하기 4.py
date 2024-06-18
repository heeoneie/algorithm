import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
sum_nums = [0]

for i in num:
    sum_nums.append(sum_nums[-1]+i)

for _ in range(m):
    i,j = map(int, input().split())
    print(sum_nums[j]-sum_nums[i-1])