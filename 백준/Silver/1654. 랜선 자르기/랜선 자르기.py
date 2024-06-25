import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
low, high = 1, max(lan)

while low <= high:
    mid = (low + high) // 2
    cnt = (sum(i // mid for i in lan))
    
    if cnt >= n:
        low = mid + 1
    else:
        high = mid - 1
    
print(high)
  