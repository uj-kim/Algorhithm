import sys
input = sys.stdin.readline

n = int(input())

#카드 값 범위가 크기 때문에 배열 인덱스로 카운트 불가
counts = {}
for _ in range(n):
  x = int(input().strip())
  counts[x] = counts.get(x, 0) + 1

sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

print(sorted_counts[0][0])