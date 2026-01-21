#슬라이딩 윈도우 알고리즘 (feat. 투포인터)
# : 2개의 포인터로 범위를 지정하여 범위(window)를 유지한 채로 이동(slide)하여 문제를 해결하는 알고리즘
# HOW ?   정해진 크기의 윈도우를 리스트의 한쪽 끝부터 다른쪽 끝까지 이동시키면서 연산 수행

# 1. 입력
s = input()
# 2. 리스트의 길이 # len(s)
# 3. 윈도우의 크기 = 문자열(s)에서 'a'의 개수
  # WHY ?  우리가 만들고 싶은 최종 상태는 연속된 'a'이기 때문에(b랑 '위치'만 교환)
  # CASE. aababa => baaaab 가 되어야함 => 연속된 a로 이루어진 범위 == 윈도우의 크기
n = s.count('a');

#4. 윈도우 구간 안에 b의 개수를 슬라이딩하면서 최소값 찾기
# 4-2. 최소값을 구하는 것이므로 
answer = float('inf')
# 4-1. 원형처리 : 리스트 2개 붙여서 이어지게 재할당
circle_s = s + s

# 4-3. 원형 s를 돌면서 윈도우크기씩 슬라이싱해서 비교
for i in range(len(s)):
  window = circle_s[i:i+n]
  answer = min(answer, window.count("b"))


# #5. 근데 1이하인 경우 예외처리 해줘야함
# if n <= 1:
#   print(0)


print(answer)
