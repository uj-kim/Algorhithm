import sys
import math

input = sys.stdin.readline


#소수 판별식
def is_prime(x):
  if x <= 1:
    return False
  for i in range(2, int(math.sqrt(x))+1):
    if x %i == 0:
      return False
  return True


while True:
  n = int(input())

  if n == 0:
    break
  cnt = 0
  for i in range(n+1, 2*n+1):
    if is_prime(i):
      cnt += 1
      
  print(cnt)