A = int(input())
B = int(input())
C = int(input())

result = A * B * C

cnt = {i: 0 for i in range(10)}

for x in str(result):
    cnt[int(x)] += 1
    
for i in range(10):
    print(cnt[i])