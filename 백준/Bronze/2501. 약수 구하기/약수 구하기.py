n, k = map(int, input().split())

q = [i for i in range(1, n+1) if n % i == 0]
print(q[k-1] if k<=len(q) else 0) 