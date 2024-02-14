import sys
input = sys.stdin.readline

num = int(input())
link = int(input())
linked = [[] for _ in range(num+1)]
visited = [False] * (num+1)

for _ in range(link):
    a,b = map(int, input().split())
    linked[a] += [b]
    linked[b] += [a]

def dfs(linked, v, visited):
    visited[v] = True
    for i in linked[v]:
        if not visited[i]:
            dfs(linked, i, visited)

dfs(linked, 1, visited)
print(visited.count(True)-1)