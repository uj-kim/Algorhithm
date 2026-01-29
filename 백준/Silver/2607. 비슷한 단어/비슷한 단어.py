from collections import Counter

n = int(input())

w = input()
w_cnt = Counter(w)

answer = 0

for _ in range(n-1):
  temp = input()
  t_cnt = Counter(temp)

  if abs(len(temp) - len(w)) >= 2:
    continue

  diff = sum((w_cnt - t_cnt).values()) + sum((t_cnt - w_cnt).values())

  if diff <= 2:
    answer += 1

print(answer)