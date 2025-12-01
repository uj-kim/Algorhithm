n = int(input())

people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

for p in people:
  rank = 1
  for o in people:
    if p[0] < o[0] and p[1] < o[1]:
      rank += 1
  print(rank, end = " ")

