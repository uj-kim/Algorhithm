import sys
from statistics import median


input = sys.stdin.readline

t = int(input())

for _ in range(t):
  m = int(input())
  arr = list(map(int, input().split()))
  while len(arr) < m:                   
    arr.extend(map(int, input().split()))

  meds = []

  for i in range(1,m+1):
    if i % 2 == 1:
      meds.append(int(median(arr[:i])))

  print(len(meds))
  for i in range(0, len(meds), 10):
        print(*meds[i:i+10])