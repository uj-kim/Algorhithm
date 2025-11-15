n, k = map(int, input().split())

#메모리초과 => k번째 숫자를 "계산"해서 찾을 것
# s = "".join(*range(1, n+1))
# print(s[k])

#구간을 나누어 k가 어느 구간에 있는지 파악해야함
#구간의 길이
nine = 9
digit = 1

while k > nine * digit:
  k -= nine * digit
  nine *= 10
  digit += 1
  
start_num = 10 ** (digit - 1)

#자릿수 구간에서 몇 번째 수인지
num_idx = (k-1) // digit
# 해당하는 수
num = start_num + num_idx
#해당 수에서 몇 번째 자리의 숫자인지
idx = (k - 1) % digit

print(-1 if num > n else str(num)[idx])