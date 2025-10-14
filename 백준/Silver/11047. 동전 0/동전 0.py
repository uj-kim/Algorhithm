import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
coins = []
cnt = 0

for _ in range(n):
  a = int(input())
  coins.append(a)

coins.sort(reverse=True)

for c in coins:
  if k == 0:
    break
  use = k // c
  cnt += use
  k %= c

print(cnt)