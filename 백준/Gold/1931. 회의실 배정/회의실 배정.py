import sys

input = sys.stdin.readline

n = int(input())
meetings = []
cnt = 1

for _ in range(n):
  s, e = map(int,input().split())
  meetings.append((e, s)) #종료시간을 기준

meetings.sort()

et = meetings[0][0]

for i in range(1, n):
  if meetings[i][1] >= et:
    et = meetings[i][0]
    cnt += 1

print(cnt)



