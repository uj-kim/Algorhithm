import sys

input = sys.stdin.readline

#입력
n = int(input())
d = list(map(int, input().split()))
cost = list(map(int, input().split()))

#초기화
min_cost = cost[0]
total = min_cost*d[0]

for i in range(1,len(cost)-1):
  if min_cost > cost[i]:
    min_cost = cost[i]
  total += min_cost*d[i]

print(total)