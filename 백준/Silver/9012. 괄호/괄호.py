t = int(input())

for _ in range(t):
  string = input()
  stack = []
    
  is_pair = True
    
  for char in string:
    if char == "(":
      stack.append(char)
    else:
      if stack:
        stack.pop()
      else:
        is_pair = False
        break
  if stack:
    is_pair = False
    
  print("YES" if is_pair else "NO") 