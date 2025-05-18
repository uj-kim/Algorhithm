from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
result = deque()

for _ in range(n):
  cmd =input().split()
  q = int(cmd[0])
  x = int(cmd[1]) if len(cmd) > 1 else None

  if q == 1:
    result.appendleft(x)
  elif q == 2:
    result.append(x)
  elif q == 3:
    print(result.popleft() if result else -1)
  elif q == 4:
    print(result.pop() if result else -1)
  elif q == 5:
    print(len(result))
  elif q == 6:
    print(1 if not result else 0)
  elif q == 7:
    print(result[0] if result else -1)
  elif q == 8:
    print(result[-1] if result else -1)