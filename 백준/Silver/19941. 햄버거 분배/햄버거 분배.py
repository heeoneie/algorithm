import sys
'''
P면 왼쪽 H을 먹어야 함
그래야 남은 P가 H를 먹을 수 있기 때문
k에 바로 걸리면 res += 1, break
'''
input = sys.stdin.readline
n,k = map(int, input().split())
HP = list(input().rstrip())
ans = 0

for i in range(n):
    if HP[i] == 'P':
        for j in range(i-k, i+k+1):
            if -1 < j < n and HP[j] == 'H':
                ans += 1
                HP[j] = '0'
                break
                
print(ans)
    