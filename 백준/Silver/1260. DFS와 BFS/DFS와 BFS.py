from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(v):
  visited[v] = True
  print(v, end=" ")
  for nxt in graph[v]:
    if not visited[nxt]:
      dfs(nxt)

def bfs(v):
  q = deque([v])
  visited[v] = True
  while q:
    cur = q.popleft()
    print(cur, end=" ")
    for nxt in graph[cur]:
      if not visited[nxt]:
        visited[nxt] = True
        q.append(nxt)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1):
  graph[i].sort()

visited = [False]*(n+1)
dfs(v)

visited = [False]*(n+1)
print()            # (선택) DFS/BFS 줄바꿈 깔끔하게
bfs(v)
