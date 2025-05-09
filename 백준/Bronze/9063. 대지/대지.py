x, y = [], []

n = int(input())

for _ in range(n):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

if n == 1:
    print(0)
else:
  print((max(x) - min(x)) * (max(y) - min(y)))