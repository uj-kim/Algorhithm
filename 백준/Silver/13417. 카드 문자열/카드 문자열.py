from collections import deque

t = int(input())

for _ in range(t):
  n = int(input())
  cards = list(input().split())
  
  dq = deque()
  dq.append(cards[0])

  for c in cards[1:]:
    if c <= dq[0]:
      dq.appendleft(c)
    else:
      dq.append(c)
  
  print("".join(dq))
