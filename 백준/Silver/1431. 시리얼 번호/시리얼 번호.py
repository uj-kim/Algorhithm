def sum_digits(s):
  return sum(int(c) for c in s if c.isdigit())

n = int(input())

nums = []

for _ in range(n):
  nums.append(input().strip())

nums.sort(key=lambda x: (len(x), sum_digits(x), x))

print("\n".join(nums))