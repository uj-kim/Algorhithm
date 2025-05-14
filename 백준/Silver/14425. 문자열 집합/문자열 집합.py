n, m = map(int, input().split()) #문자열 개수

s_set = {input() for _ in range(n)}
m_list = [input() for _ in range(m)]

cnt = sum(1 for word in m_list if word in s_set)

print(cnt)