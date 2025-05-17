n = int(input())

stack = []
current = 1

people = list(map(int, input().split()))

for student in people:
  while stack and stack [-1] == current:
    stack.pop()
    current += 1
  
  if student == current:
    current += 1
  else:
    stack.append(student)

while stack and stack[-1] == current:
  stack.pop()
  current += 1

print("Nice" if not stack else "Sad")
