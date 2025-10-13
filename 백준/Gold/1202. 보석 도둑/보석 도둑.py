import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
h = []
gems = []
bags = []

# 입력
for _ in range(n):
  m, v = map(int, input().split())
  gems.append((m,v))

for _ in range(k):
  c = int(input())
  bags.append(c)

# 보석 무게, 가방용량 오름차순 정렬
gems.sort()
bags.sort()

#최대힙 => 가방에 넣을 수 있는 보석들 추가
i = 0 #인덱스
answer = 0

for c in bags:
  while i < len(gems) and gems[i][0] <= c:
    heapq.heappush(h, -gems[i][1])
    i += 1 #인덱스전진

  #최대 가치 뽑기 
  if h:
    answer += -heapq.heappop(h)

#결과출력
print(answer)
