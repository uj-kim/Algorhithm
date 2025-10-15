import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

reminders = [0] * m
reminders[0] = 1

prefix_sum = 0
result = 0

for x in arr:
  prefix_sum = (prefix_sum + x) % m
  result += reminders[prefix_sum]
  reminders[prefix_sum] += 1
  
print(result)