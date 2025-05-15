def find_gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def find_lcm(a, b):
  return a * b // find_gcd(a, b)

T = int(input())

for _ in range(T):
  a, b = map(int, input().split())
  print(find_lcm(a, b))
