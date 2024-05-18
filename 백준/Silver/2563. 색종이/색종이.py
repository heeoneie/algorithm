n = int(input())
size = [[0 for _ in range(101)]for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split()) # 3~13, 7~17 | 5~15, 2~12 | 15~25 7~17
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            size[j][i] = 1

cnt = 0
for row in size:
    cnt = cnt + row.count(1)
print(cnt)