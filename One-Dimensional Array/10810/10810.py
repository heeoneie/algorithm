N,M = map(int, input().split())
box = [0]*N

for _ in range(M):
    i,j,k = map(int, input().split())
    for n in range(i,j+1):
        box[n-1] = k
        
for n in range(N):
    print(box[n],end=' ')
