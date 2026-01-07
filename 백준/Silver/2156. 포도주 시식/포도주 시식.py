n = int(input())
dp = [0] * (n)
juice = []
for _ in range(n):
  juice.append(int(input()))
#목표 : 가장 많은 포도주 마시기
#조건은 3잔부터 적용되므로 2잔까지는 모두 마시는 게 이득.
if n >= 1:
  dp[0] = juice[0]
if n >= 2: 
  dp[1] = juice[0] + juice[1]

#여기서부터 조건2가 적용(3잔 이상 -> 3잔 연속으로 못 마시므로 경우를 나눠서 생각)

for i in range(2, n):
  dp[i] = max(
    #1. 이전에 2잔을 마신 경우(마시고, 마신 경우 -> 이번에 못 마심)
    dp[i-1], #dp가 누적값이므로 이전 dp
    #2. 마시고, 안 마시고, 이제 마실 차례인 경우
    dp[i-2] + juice[i],
    #3. 안 마시고, 마시고, 또 마시는 경우
    (dp[i-3] if i>= 3 else 0) + juice[i-1] + juice[i]
  )

print(dp[n-1])