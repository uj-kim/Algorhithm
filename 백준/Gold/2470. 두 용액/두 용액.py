import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

left, right = 0, n - 1
best = float('inf')


while left < right:
  s = nums[left] + nums[right]
  if best > abs(s):
    best = abs(s)
    best_left, best_right = nums[left], nums[right]
  
  elif s < 0:
    left += 1
  else:
    right -= 1

print(best_left, best_right)


