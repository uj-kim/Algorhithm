from itertools import permutations

n, k = map(int, input().split())
kits = list(map(int, input().split()))

ans = 0
for kit in permutations(kits, n):
    w = 500
    ok = True
    for kw in kit:
        w += kw - k
        if w < 500:
            ok=False
            break
    if ok:
        ans += 1

print(ans)
