import sys

input = sys.stdin.readline

n, c = map(int, input().split())

houses = [int(input()) for _ in range(n)]

houses.sort()

#각 집의 거리(distance)
start, end = 1, houses[-1] - houses[0]
max_d = 0

while start <= end:
  mid = (start + end) // 2
  current = houses[0]
  cnt = 1 #첫번째 집에 공유기 1대 설치
  
  for x in houses:
    if x >= current + mid:
      cnt += 1
      current = x
  
  if cnt >= c:
    max_d = max(max_d, mid)
    start = mid + 1
  else:
    end = mid - 1

print(max_d)