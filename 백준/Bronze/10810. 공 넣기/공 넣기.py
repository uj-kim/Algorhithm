'''
바구니 개수 : N개
공을 던지는 횟수 : M번
'''

N, M = map(int, input().split())

basket = [0] * N   #처음에는 바구니에 아무 공도 들어있지 않음.

for _ in range(M):
  i, j, k = map(int, input().split())
  for x in range(i-1, j):
    basket[x] = k

print(*basket)