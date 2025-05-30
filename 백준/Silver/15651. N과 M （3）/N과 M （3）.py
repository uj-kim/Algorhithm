def backtracking(x):
  if len(x) == m:
    print(' '.join(map(str, x)))
    return

  for i in range(1, n+1):
      x.append(i)
      backtracking(x)
      x.pop()

n, m = map(int, input().split())

backtracking([])