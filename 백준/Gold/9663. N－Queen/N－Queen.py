import sys
input = sys.stdin.readline

n = int(input())

cols = set()
diag1 = set() #우하향 대각선
diag2 = set() #우상향 대각선
ans = 0

def backtrack(r: int):
  global ans

  if n == r:
    ans += 1
    return
  
  for x in range(n):
    if x in cols or (r-x) in diag1 or (r+x) in diag2:
      continue
    cols.add(x); diag1.add(r-x); diag2.add(r+x)
    backtrack(r+1)

    cols.remove(x); diag1.remove(r-x); diag2.remove(r+x)

backtrack(0)
print(ans)
