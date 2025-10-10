import sys
import heapq

input = sys.stdin.readline
min_abs_heap = []
output = []

n = int(input())

for _ in range(n):
  x = int(input())
  
  if x == 0:
    if min_abs_heap:
      output.append(heapq.heappop(min_abs_heap)[1])
    else:
      output.append(0)
  
  else:
    heapq.heappush(min_abs_heap, (abs(x),x))


for i in output:
  print(i)