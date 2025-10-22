import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
h_low, h_high = 0, max(trees)

while h_low <= h_high:
  got = 0
  mid = (h_low+h_high) // 2

  for t in trees:
    if t > mid:
      got += t - mid

  if got < m:
    h_high = mid - 1
  else:
    h_low = mid + 1

print(h_high)
