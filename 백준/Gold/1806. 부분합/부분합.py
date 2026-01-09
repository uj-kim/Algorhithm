import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
min_length = float('inf')
cur_sum = 0

while True:
  if cur_sum >= s:
    min_length = min(min_length, r - l)
    cur_sum -= arr[l]
    l += 1
  else: 
    if r == n:
      break
    cur_sum += arr[r]
    r += 1

print(0 if min_length == float('inf') else min_length)

