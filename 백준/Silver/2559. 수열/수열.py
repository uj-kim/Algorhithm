n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]*(n+1)

#누적합 구하기
for i in range(1, n+1):
  prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

#최대온도 초기화
max_sum = -100*k

# arr[i:i+k]의 합
# i는 n-k+1까지 가능
for i in range(n-k+1):
  current_sum = prefix_sum[i+k] - prefix_sum[i]
  if current_sum > max_sum:
    max_sum = current_sum

print(max_sum)