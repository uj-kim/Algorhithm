s = input()

suffixes = sorted(s[i:] for i in range(len(s)))

for c in suffixes:
  print(c)