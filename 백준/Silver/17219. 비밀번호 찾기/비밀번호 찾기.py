#1. 저장된 사이트 주소의 수 : n
# 비밀번호 찾으려는 사이트 수 : m
n, m = map(int, input().split())

# 딕셔너리 형태로 입력값 [주소] = PW 저장 
pw_book = {}

for _ in range(n):
  url, pw = map(str, input().split())
  pw_book[url] = pw

for _ in range(m):
  need_to_find = input()
  print(pw_book[need_to_find])
