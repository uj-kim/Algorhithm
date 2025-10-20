import sys

input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for x in targets:
  if x in arr:
    print(1)
  else:
    print(0)
