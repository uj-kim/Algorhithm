n = int(input())

powers = [list(map(int, input().split())) for _ in range(n)]

selected = [False] * n # True -> 스타트팀, False -> 링크팀
selected[0] = True #0번 사람은 무조건 스타트팀

answer = float('inf')


# 백트래킹 함수 상태 설정
# idx : 지금 몇 번째 사람을 보고 있는지
# cnt : 현재까지 스타트팀의 인원

#dfs
def dfs(idx, cnt):
  global answer
  # 불필요한 경우
  if cnt > n // 2 or (n - idx) < (n // 2 - cnt):
    return

  # 팀이 완성된 경우
  if idx == n:
    if cnt == n // 2:
      start_power = link_power = 0
      for i in range(n):
        for j in range(i + 1, n):
          if selected[i] and selected[j]:
            start_power += powers[i][j] + powers[j][i]
          elif not selected[i] and not selected[j]:
            link_power += powers[i][j] + powers[j][i]
      answer = min(answer, abs(start_power-link_power))
    return

  # idx 위치에 있는 사람을 스타트 팀에 합류
  selected[idx] = True
  # 위치 전진, 스타트팀 인원추가
  dfs(idx + 1, cnt + 1)

  # idx 위치에 있는 사람을 링크 팀에 합류
  # 위치 전진, 스타트 팀 인원 유지
  selected[idx] = False
  dfs(idx + 1, cnt)

dfs(1, 1)
print(answer)