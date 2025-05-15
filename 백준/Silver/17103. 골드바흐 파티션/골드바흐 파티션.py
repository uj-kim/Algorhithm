import sys
import math

input = sys.stdin.readline

#에라토스테네스의 체
#max를 지정
#2의 배수 제거 -> 그다음 소수의 배수 제거 (반복)

max_range = 1000000
#소수 판별 리스트
prime_list = [True] * (max_range + 1)
#0과 1은 소수가 아니므로
prime_list[0] = prime_list[1] = False

#에라토스테네스의 체
for i in range(2, int(math.sqrt(max_range)) + 1):
  if prime_list[i]:
    for j in range(i*i, max_range +1, i):
      prime_list[j] = False

#테스트 케이스
T = int(input())

for _ in range(T):
  n = int(input())
  cnt = 0

  for i in range(2, n //2 +1):
    # i + j == n
    if prime_list[i] and prime_list[n-i]:
      cnt += 1

  print(cnt)