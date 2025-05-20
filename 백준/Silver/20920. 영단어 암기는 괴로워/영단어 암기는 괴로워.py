import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = []

for _ in range(n):
  word = input().strip()
  if len(word) >= m:
    words.append(word)

counter = Counter(words)
sorted_words = sorted(counter.items(),key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
  print(word)
