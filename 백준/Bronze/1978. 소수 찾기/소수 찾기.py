import math

n = int(input())
nums = list(map(int, input().split()))

def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(math.isqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

primes = [num for num in nums if is_prime(num)]

print(len(primes))
