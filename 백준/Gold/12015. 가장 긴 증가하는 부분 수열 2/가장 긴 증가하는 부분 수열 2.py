import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

tails = []

for x in a:
    lo, hi = 0, len(tails)
    while lo < hi:
        mid = (lo + hi) // 2

        if tails[mid] < x:
            lo = mid + 1
        else:
            hi = mid

    if lo == len(tails):
        tails.append(x)
    else:
        tails[lo] = x

print(len(tails))