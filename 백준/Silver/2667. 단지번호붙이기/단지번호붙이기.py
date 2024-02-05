def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        global home
        home += 1
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
town = []
home = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            town.append(home)
            home = 0
            
print(len(town))
town.sort()
for i in range(len(town)):
    print(town[i])
    