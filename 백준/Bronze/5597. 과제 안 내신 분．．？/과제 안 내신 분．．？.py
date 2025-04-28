#set, 차집합 이용
all_students = set(range(1, 31))
submitted = set()

for _ in range(28):
  submitted.add(int(input()))

missing = sorted(all_students - submitted)

print(missing[0])
print(missing[1])