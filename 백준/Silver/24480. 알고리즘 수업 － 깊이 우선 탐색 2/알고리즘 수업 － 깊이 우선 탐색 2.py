import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(graph, visited, order, v, cnt):
    visited[v] = True
    order[v] = cnt
    cnt += 1
    
    for u in sorted(graph[v], reverse=True):
        if not visited[u]:
            cnt = dfs(graph, visited, order, u, cnt)
    return cnt

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (n+1)
order = [0] * (n+1)
dfs(graph, visited, order, r, 1)

for i in range(1,n+1):
    print(order[i])