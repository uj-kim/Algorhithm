import sys
input = sys.stdin.readline

n = int(input())
people = set(["ChongChong"])

for _ in range(n):
  a, b = input().split()
  if a in people or b in people:
    people.add(a)
    people.add(b)

print(len(people))