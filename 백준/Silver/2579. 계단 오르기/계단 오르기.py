n = int(input())

steps = []
#규칙
# 계단은 1step or 2step
# 3계단을 연속해서 밟을 수 없음
# 도착계단 반드시 포함

for _ in range(n):
  steps.append(int(input()))

dp = [0]*n

# 2step까지는 되니까
if len(steps) <= 2:
  print(sum(steps))

else:
  #dp[i] : i번째 계단까지 왔을 때의 최대점수(여러가지 경우의 수 중 max)
  dp[0] = steps[0]
  dp[1] = steps[0] + steps[1] #연속2개까진 괜찮잖아
  # 3번째 계단부터 문제
  # 계단1->계단3, 계단2->계단3
  dp[2] = max(steps[0] + steps[2], steps[1] + steps[2])

  for i in range(3, n):
    dp[i]= max(dp[i-2] + steps[i], dp[i-3]+steps[i-1]+steps[i])

  print(dp[-1])
