from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

n = int(input())

for _ in range(n):
  cmd = input().strip().split()
  q = cmd[0]
  x = cmd[1] if len(cmd) > 1 else None

  if q == "push":
    queue.append(int(x))
  
  elif q == "pop":
    print(queue.popleft() if queue else -1)

  elif q =="size":
    print(len(queue))

  elif q == "empty":
    print(1 if not queue else 0)

  elif q == "front":
    print(queue[0] if queue else -1)

  elif q == "back":
    print(queue[-1] if queue else -1)