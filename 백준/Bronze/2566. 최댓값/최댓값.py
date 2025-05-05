A = [list(map(int, input().split())) for _ in range(9)]

max_value = max(map(max,A))

for i, row in enumerate(A):
  if max_value in row:
    j = row.index(max_value)
    print(max_value)
    print(i+1, j+1)
    break