#set()으로 좌표를 입력받아서 영역계산
covered = set()

#도화지 수
n = int(input())

for _ in range(n):
  x, y = map(int, input().split()) #좌표값 받기
  for i in range(x, x+10):
    for j in range(y, y+10):
      covered.add((i, j))

print(len(covered))