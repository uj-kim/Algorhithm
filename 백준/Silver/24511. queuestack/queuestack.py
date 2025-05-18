from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque()

for a, b in zip(A, B):
  if a == 0:
    q.append(b)
  
for c in C:
  q.appendleft(c)
  print(q.pop(), end = ' ')
  
