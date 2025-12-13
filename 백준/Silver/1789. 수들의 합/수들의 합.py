s = int(input())

total = 0
cnt = 0
cur = 1

while total + cur <= s:
  total += cur
  cur += 1
  cnt += 1

print(cnt)