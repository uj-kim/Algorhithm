import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]

lo, hi = 1, max(lengths)

while lo <= hi:
  mid = (lo + hi) // 2
  cnt = 0
  for l in lengths:
    cnt += l // mid
    
  if cnt >= n:
    lo = mid + 1
  else:
    hi = mid - 1

print(hi)
    