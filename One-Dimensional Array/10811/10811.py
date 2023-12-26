N,M = map(int, input().split())
box = [i for i in range(N+1)]

for _ in range(M):
    i,j = map(int, input().split())
    box[i:j+1] = reversed(box[i:j+1])
    
box.remove(box[0])
print(*box)
