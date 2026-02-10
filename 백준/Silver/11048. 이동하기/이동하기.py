n, m = map(int, input().split())

maze = []

#미로(2차원 배열) 형성
for i in range(n):
  maze.append(list(map(int, input().split())))

#준규가 움직일 수 있는 방향은 하, 우, 대각선아래

#dp 활용, 최대 누적 사탕 수 구하기
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    prev_dp = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    cur = maze[i-1][j-1]

    #현재 최대 누적 사탕 개수는
    dp[i][j] = prev_dp + cur

print(dp[n][m])