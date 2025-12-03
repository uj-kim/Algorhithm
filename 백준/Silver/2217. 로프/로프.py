n = int(input())

ropes = []

for _ in range(n):
  w = int(input())
  ropes.append(w)

ropes.sort()

answer = 0
for i in range(n):
  w = ropes[i] * (n-i)
  answer = max(answer, w) 

print(answer)