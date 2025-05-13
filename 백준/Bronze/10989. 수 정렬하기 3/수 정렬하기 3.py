#메모리초과
#해결법 : 계수정렬(Counting Sort)
#계수 정렬 조건
#1. 데이터 범위가 제한
#2. 데이터는 양의 정수
#3. 가장 큰 데이터와 가장 작은 데이터의 차가 백만을 넘지 않음
# => 입력값은 1부터 10,000까지의 자연수이므로 모두 해당됨.
import sys

input = sys.stdin.readline

n = int(input())
#가장 작은 데이터부터 가장 큰 데이터까지 모두 담는 리스트 생성
#원소의 최대값까지 인덱싱할 수 있도록 배열 길이는 원소의 최대값 + 1
x = [0] * 10001
for _ in range(n):
  # x.append(int(input()))
  #입력된 데이터와 동일한 인덱스의 데이터를 1증가
  x[int(input())] += 1

#배열에서 0인 값을 제외하고 인덱스를 인덱스 값만큼 출력
for i in range(1, 10001):
  for _ in range(x[i]):  # 메모리를 아끼기 위해 한 줄씩 출력
        sys.stdout.write(f"{i}\n")