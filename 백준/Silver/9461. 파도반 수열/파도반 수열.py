import sys

input = sys.stdin.readline

t = int(input())

queries = [int(input()) for _ in range(t)]

max_n = max(queries)

p = [0] * (max(6, max_n+1))

p[1], p[2], p[3], p[4], p[5] = 1, 1, 1, 2, 2

for i in range(6, max_n + 1):
    p[i] = p[i - 2] + p[i - 3]

for n in queries:
    print(p[n])