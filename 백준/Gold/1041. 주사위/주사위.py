import sys

input = sys.stdin.readline
n = int(input())
dice = list(map(int, input().split()))
#(A,F), (B,E), (C,D)
#보이는 면이 가장 작으려면
#1개의 면만 보이는 주사위(min1) => min(dice)
#2개의 면만 보이는 주사위(min2) => 서로 인접한 2면 중 최소
#3개의 면만 보이는 주사위(min3) => 서로 인접한 3면 조합중 최소
#각 주사위의 개수 곱해서 더해주면 답
# min3는 항상 4개로 고정
# min2의 개수는 4(2n-3)
# min1의 개수는 (n-2)(5n-6)

# 예외 처리 : n = 1인경우, 면이 5면
if n == 1:
  print(sum(dice) - max(dice))

else:

  # 인접한 요소들의 최소 합 구하기
  sum_list = []
  sum_list.append(min(dice[0], dice[5]))
  sum_list.append(min(dice[1], dice[4]))
  sum_list.append(min(dice[2], dice[3]))
  
  sum_list.sort()
  
  min1 = sum_list[0]
  min2 = min1 + sum_list[1]
  min3 = min2 + sum_list[2]
  
  # 개수 공식 적용
  count1 = (n - 2) * (5 * n - 6)
  count2 = 4 * (2 * n - 3)
  count3 = 4
  
  result = min1 * count1 + min2 * count2 + min3 * count3
  
  print(result)