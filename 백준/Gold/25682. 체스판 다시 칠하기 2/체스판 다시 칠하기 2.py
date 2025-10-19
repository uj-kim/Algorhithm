import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

board = [input().strip() for _ in range(n)]

startB = [[0]*m for _ in range(n)]

for i in range(n):
  for j in range(m):
    expectB = ((i+j) % 2 == 0)
    currentB = (board[i][j] == 'B')

    #B로 시작한다면
    if expectB != currentB:
      startB[i][j] = 1

#누적합
ps = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
  row = startB[i-1]
  for j in range(1, m+1):
    ps[i][j] = row[j-1] + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

#K*K 평가
result = float("inf")
for x_start in range(1, n-k+2):
  for y_start in range(1, m-k+2):
    x_end = x_start + k - 1
    y_end = y_start + k - 1
    sumB = ps[x_end][y_end] - ps[x_start-1][y_end] - ps[x_end][y_start-1] + ps[x_start-1][y_start-1]

    sumW = k * k - sumB

    result = min(result, sumB, sumW)

print(result)