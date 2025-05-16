import sys

input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
  nums = input().split()
  num = int(nums[0])
  x = int(nums[1]) if len(nums) > 1 else None

  if num == 1:
    stack.append(x)
  
  if num == 2:
    if stack:
        print(stack.pop())
    else:
      print(-1)
  
  if num == 3:
    print(len(stack))

  if num == 4:
    print(1 if len(stack) == 0 else 0)
  
  if num == 5:
    print(stack[-1] if stack else -1)
  
