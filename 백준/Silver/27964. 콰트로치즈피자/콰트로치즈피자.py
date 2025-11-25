n = int(input())

toppings = input().split()
cheese = {}
isQuattro = 0

for c in toppings:
  if c[-6:] == "Cheese" and c not in cheese:
    cheese[c] = cheese.get(c, 0) + 1
    isQuattro += 1

    if isQuattro == 4:
      break

print("yummy" if isQuattro == 4 else "sad")

