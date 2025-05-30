def backtracking(x, start):
  if len(x) == m:
    print(' '.join(map(str, x)))
    return

  for i in range(start, n+1):
      x.append(i)
      backtracking(x, i)
      x.pop()

n, m = map(int, input().split())
backtracking([], 1)