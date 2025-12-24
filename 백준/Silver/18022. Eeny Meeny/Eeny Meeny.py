from collections import deque

s = input().split()
n = int(input())

dq = deque()

teamA, teamB = [], []
team_toggle = True

for _ in range(n):
  dq.append(input())

while dq:
  dq.rotate(-(len(s) - 1))
  if team_toggle:
    teamA.append(dq.popleft())
  else:
    teamB.append(dq.popleft())
  team_toggle = not team_toggle

print(len(teamA))
print(*teamA, sep="\n")
print(len(teamB))
print(*teamB, sep="\n")