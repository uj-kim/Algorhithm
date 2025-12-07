n, m = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 0
cur_sum = 0
cnt = 0

while right < len(arr):
    cur_sum += arr[right]

    while cur_sum > m:
      cur_sum -= arr[left]
      left += 1
    
    if cur_sum == m:
      cnt += 1
    
    right += 1

print(cnt)