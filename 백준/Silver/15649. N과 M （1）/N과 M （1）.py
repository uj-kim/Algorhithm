n, m = map(int, input().split())

arr = list(range(1,n+1))
visited = [False] * (n+1)
result = []

def backtrack(arr):
  if len(result) == m:
    print(' '.join(map(str, result)))
  
  for i in arr:
    if not visited[i]:
      visited[i] = True
      result.append(i)
      backtrack(arr)
      result.pop()
      visited[i] = False

backtrack(arr)