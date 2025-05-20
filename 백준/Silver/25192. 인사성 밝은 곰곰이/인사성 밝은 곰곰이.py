import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
visit = set()

for _ in range(n):
  user = input().strip()
  if user == "ENTER":
    visit.clear()
  elif user not in visit:
    visit.add(user)
    cnt += 1

print(cnt)

