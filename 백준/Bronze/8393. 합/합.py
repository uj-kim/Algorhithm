from functools import reduce

n = int(input())
result = list(range(1, n+1))
print(reduce(lambda a, b: a + b, result))
