import math

m = int(input())
n = int(input())

def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(math.isqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

primes = [num for num in range(m, n+1) if is_prime(num)]

if len(primes) == 0:
  print(-1)
else:
  print(sum(primes))
  print(min(primes))