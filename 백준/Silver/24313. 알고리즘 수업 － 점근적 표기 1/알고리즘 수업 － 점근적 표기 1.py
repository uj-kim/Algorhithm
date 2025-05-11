a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if n0 * (a1 -c) + a0 <= 0 and a1<= c:
    print(1)
else:
    print(0)