n = int(input())
for i in range(max(1,n-9*len(str(n))), n+1):
  sum_i = sum(map(int, str(i)))
  if i + sum_i == n:
    print(i)
    break
else:
  print(0)