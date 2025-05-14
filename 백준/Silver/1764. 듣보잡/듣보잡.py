n, m = map(int, input().split())
never_heard_set = {input() for _ in range(n)}
never_seen_set = {input() for _ in range(m)}

never_set = never_heard_set & never_seen_set
print(len(never_set))
for i in sorted(never_set):
  print(i)