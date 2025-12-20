from collections import deque

answer = []

n = int(input())
dq = deque(range(1, n+1))

while len(dq) > 1:
  answer.append(dq.popleft())
  dq.rotate(-1)

answer.append(dq.pop())

print(*answer)