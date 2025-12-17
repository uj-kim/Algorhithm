t = int(input())
for _ in range(t):
  n = int(input())
  note1 = set(map(int, input().split()))
  m = int(input())
  note2 = list(map(int, input().split()))

  for x in note2:
    print(1 if x in note1 else 0)