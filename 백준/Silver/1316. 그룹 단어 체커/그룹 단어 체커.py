#입력받을 단어 개수
n = int(input())

#그룹 단어 카운트
cnt = 0

for _ in range(n):
  word = input()
  used = set()
  temp = ''
  is_group = True

  for c in word:
    if c != temp:
      if c in used:
        is_group = False
        break;

      used.add(c)
    temp = c
  
  if is_group:
    cnt += 1

print(cnt)

