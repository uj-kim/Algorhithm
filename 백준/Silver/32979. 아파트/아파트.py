from collections import deque

n = int(input())
t = int(input())

dq = deque(list(map(int, input().split())))

targets = list(map(int, input().split()))

for x in targets:
  # for _ in range(targets[i]):
    # dq.append(dq.popleft())
  dq.rotate(-(x-1))
  print(dq[0], end = ' ')