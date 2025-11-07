import sys
input = sys.stdin.readline

n, m = map(int, input().split())

path = [0]*m
result = []

def backtrack(depth):
  if depth == m:
    result.append(' '.join(map(str, path)))
    return
  
  for x in range(1, n+1):
    path[depth] = x
    backtrack(depth + 1)

backtrack(0)
sys.stdout.write('\n'.join(result))
