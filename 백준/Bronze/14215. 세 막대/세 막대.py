a, b, c = map(int, input().split())

# 가장 긴 변 >= 두 변의 합 -> invalid
sides = sorted([a, b, c])

if sides[2] >= sides[0] + sides[1]:
  print(2*(sides[0] + sides[1]) - 1)
else:
  print(sum(sides))