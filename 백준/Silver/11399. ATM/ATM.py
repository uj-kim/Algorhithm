import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()

acc = 0
total = 0

for x in p:
  acc += x
  total += acc

print(total)

