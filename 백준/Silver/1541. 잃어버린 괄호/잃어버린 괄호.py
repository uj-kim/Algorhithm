import sys

input = sys.stdin.readline

#'-'를 기준으로 1차 나눔
s = input().strip().split('-')
chunks = []
for chunk in s:
  #1차에서 '+'를 기준으로 숫자분리
  nums = [int(t) for t in chunk.split('+') if t]
  #분리된 숫자들의 합
  chunks.append(sum(nums))

print(chunks[0] - sum(chunks[1:]))

