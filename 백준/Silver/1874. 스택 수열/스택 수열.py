stack = []
answer = []
cur = 1
ok = True

n = int(input())

for _ in range(n):
    x = int(input())

    while cur <= x:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack and stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        ok = False
        break

if not ok:
    print("NO")
else:
    print("\n".join(answer))
