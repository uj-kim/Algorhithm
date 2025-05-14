n = int(input())
people = set()

for _ in range(n):
  name, action = input().split()
  if action == "enter":
    people.add(name)
  else:
    people.remove(name)

for name in sorted(people, reverse=True):
  print(name)