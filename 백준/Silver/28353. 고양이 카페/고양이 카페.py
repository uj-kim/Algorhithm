#고양이의 수와 무게 k
n, k = map(int, input().split())
#각 고양이의 무게 
cats = list(map(int, input().split()))
#무게 오름차순 정렬
cats.sort()

# 2마리 세트를 최대한 많이 만들려면,
# 가장 무거운 고양이를 처리
# 가장 무거운 고양이가 가장 가벼운 고양이랑도 해결이 안 된다면 어떤 고양이로도 세트 X
# => 가장 적게 나가는 고양이 + 가장 무거운 고양이 조합
# 배열의 양 끝 인덱스를 나타낼 변수
l, r = 0, n - 1
# 정답을 출력할 변수(행복해질 수 있는 사람 수)
answer = 0

# 두 포인터로 조합 좁히기
while l < r:
  if cats[l] + cats[r] <= k:
    answer += 1
    l += 1
    r -= 1
  else:
    r -= 1

print(answer)


