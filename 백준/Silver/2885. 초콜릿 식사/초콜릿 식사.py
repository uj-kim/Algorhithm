K = int(input())

# 1. 최소 초콜릿 크기
size = 1
while size < K:
    size *= 2

# 2. 쪼개는 횟수
cnt = 0
cur = size

while K > 0:
    if cur <= K:
        K -= cur
    else:
        cur //= 2
        cnt += 1

print(size, cnt)
