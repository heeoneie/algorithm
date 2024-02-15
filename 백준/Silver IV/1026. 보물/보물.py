import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) # 1 1 1 6 0
b = list(map(int, input().split())) # 2 7 8 3 1
s = []
# a의 최솟값을 뺀다 B의 최댓값 빼고 -> n번 반복
for _ in range(n):
    min_a = min(a)
    a.remove(min_a)
    max_b = max(b)
    b.remove(max_b)
    s.append(min_a*max_b)

print(sum(s))