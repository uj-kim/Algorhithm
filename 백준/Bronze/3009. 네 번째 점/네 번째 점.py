x, y = [], []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

print(*(c[0] ^ c[1] ^ c[2] for c in (x, y)))