x = []

for _ in range(5):
  x.append(int(input()))

x.sort()
print(sum(x) // 5)
print(x[2])