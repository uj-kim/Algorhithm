t = int(input())

for _ in range(t):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input().strip())
    numbers.sort()

    is_ok = True
    for i in range(n - 1):
        if numbers[i+1].startswith(numbers[i]):
            is_ok = False
            break

    print("NO" if not is_ok else "YES")
