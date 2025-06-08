import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
for num in numbers:
    prefix_sum.append(prefix_sum[-1] + num)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])