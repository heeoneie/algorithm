N,M = map(int, input().split())
box = list()
temp = 0
for i in range(1,N+1):
    box.append(i)

for _ in range(M):
    i,j = map(int, input().split())
    temp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = temp
    
for i in range(N):
    print(box[i],end=" ")
    
