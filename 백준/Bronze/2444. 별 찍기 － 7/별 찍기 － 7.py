n = int(input())

#다이아몬드 별찍기

#위쪽 삼각형
for i in range(1, n+1):
  print(' '*(n-i) + '*'*(2*i - 1))

#아래쪽 삼각형
for i in range(n-1, 0, -1):
  print(' '*(n-i) + '*'*(2*i -1))