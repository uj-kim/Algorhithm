cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c in cr:
  word = word.replace(c, 'A')

print(len(word))