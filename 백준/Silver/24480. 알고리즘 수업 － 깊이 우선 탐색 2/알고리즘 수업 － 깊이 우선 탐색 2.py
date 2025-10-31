import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 정점 내림차순 방문
for i in range(1, n + 1):
    graph[i].sort(reverse=True)

order = [0] * (n + 1)
cnt = 1

stack = [r]
while stack:
    u = stack.pop()
    if order[u] != 0:
        continue
    order[u] = cnt
    cnt += 1

    for v in reversed(graph[u]):
        if order[v] == 0:
            stack.append(v)

print("\n".join(str(order[i]) for i in range(1, n + 1)))
