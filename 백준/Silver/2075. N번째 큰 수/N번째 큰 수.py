import sys
import heapq

input = sys.stdin.readline

n = int(input())
t = []

for _ in range(n):
  for x in map(int, input().split()):
    if len(t) < n:
      heapq.heappush(t, x)
    else:
      if x > t[0]:
        heapq.heapreplace(t, x)


print(t[0])