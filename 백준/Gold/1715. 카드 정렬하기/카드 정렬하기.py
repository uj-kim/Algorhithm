import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  heapq.heappush(heap, int(input()))

result = 0

while len(heap) > 1:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  s = a + b
  result += s
  heapq.heappush(heap, s)

print(result)