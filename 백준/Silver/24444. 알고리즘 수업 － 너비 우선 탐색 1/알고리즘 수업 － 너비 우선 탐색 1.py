from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
visited[r] = 1
queue = deque([r])
cnt = 1

while queue:
    current = queue.popleft()
    for i in sorted(graph[current]):
        if not visited[i]:
            queue.append(i)
            cnt += 1
            visited[i] = cnt

for i in visited[1:]:
    print(i)