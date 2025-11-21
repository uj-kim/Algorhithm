import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))
diffs = []

#인접키차이
for i in range(n-1):
  diffs.append(heights[i+1] - heights[i])

diffs.sort()

#가장 작은 n-k개의 차이만 더하기
print(sum(diffs[:n-k]))