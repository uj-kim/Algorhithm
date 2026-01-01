n = int(input())
m = []
for i in range(n):
    w, h = map(int, input().split())
    m.append((w*w + h*h, i+1))   # 대각선 픽셀^2

m.sort(key=lambda x: (-x[0], x[1]))  # 값 내림차순, 번호 오름차순

for _, idx in m:
    print(idx)