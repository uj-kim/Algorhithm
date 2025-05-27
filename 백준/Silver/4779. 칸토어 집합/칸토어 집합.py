import sys

def cantor(x):

  if len(x) == 1:
    return x
# 3등분
  left = cantor(x[0:len(x)//3])
  mid = ' ' * (len(x)//3)
  right = cantor(x[2*len(x)//3:])

  return left + mid + right

for l in sys.stdin:
  s = '-'*(3**(int(l.strip())))
  print(cantor(s))