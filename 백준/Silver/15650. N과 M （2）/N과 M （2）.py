n, m = map(int, input().split())

arr = list(range(1,n+1))
result = []

def backtrack(start):
  if len(result) == m:
    print(' '.join(map(str, result)))
    return
  for i in range(start, n):
      result.append(arr[i])
      backtrack(i+1)
      result.pop()

backtrack(0)

