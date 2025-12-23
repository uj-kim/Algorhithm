n = int(input())

fruits = list(map(int, input().split()))

left, right = 0, 0
max_len = 0
fruits_count = {}

while right < n:
  #fruits[right]을 fruits_count에 추가
  f = fruits[right]
  fruits_count[f] = fruits_count.get(f, 0) + 1

  #종류가 2개 초과인 경우 left를 이동하면서 줄인다
  while len(fruits_count) > 2:
    lf = fruits[left]
    fruits_count[lf] -= 1
    if fruits_count[lf] == 0:
      del fruits_count[lf]
    left += 1
  max_len = max(max_len, right - left + 1)
  right += 1

print(max_len)