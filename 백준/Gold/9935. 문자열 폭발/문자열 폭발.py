import sys

input = sys.stdin.readline

stack = []

s = input().strip()
x = input().strip()

for ch in s:
  stack.append(ch)

  if ''.join(stack[-len(x):]) == x:
    del stack[-len(x):]

print('FRULA' if not stack else ''.join(stack))