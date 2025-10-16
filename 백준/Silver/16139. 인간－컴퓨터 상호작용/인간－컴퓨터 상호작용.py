import sys

input = sys.stdin.readline

s = input().strip() #입력문자열
q = int(input()) #질문의 수

'''
for _ in range(q):
  a, l, r = input().split(' ')
  l = int(l)+1
  r = int(r)

  print(s[l:r].count(a))
'''
#s[l:r]에서 a의 개수는
#s[:r+1]에서 a의 개수 - s[:l]에서의 a의 개수
#과거 스냅샷을 저장해두면 편하게 활용 가능

#알파벳 26개별 s[:i]에서의 누적 개수를 저장
n = len(s)
prefix = [[0]*26 for _ in range(n+1)]

#prefix 채우기
for i, c in enumerate(s):
  #알파벳 인덱싱(a~z -> 0~25로 맞춤)
  idx = ord(c) - ord('a')
  
  #알파벳 누적
  prefix[i+1] = prefix[i][:]
  prefix[i+1][idx] += 1

#문제받기
for _ in range(q):
  a, l, r = input().strip().split()

  l = int(l)
  r = int(r)

  #찾을 문자 인덱스 변환
  new_a = ord(a) - ord('a')

  print(prefix[r+1][new_a] - prefix[l][new_a])