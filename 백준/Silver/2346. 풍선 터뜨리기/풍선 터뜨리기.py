from collections import deque

n = int(input())
nums = list(map(int,input().split()))
balloons = deque((i + 1, num) for i, num in enumerate(nums))
result = []

while balloons:
  idx, paper = balloons.popleft()
  result.append(idx)

  if paper > 0 :
    balloons.rotate(-(paper-1))
  else:
    balloons.rotate(-paper)
print(*result)