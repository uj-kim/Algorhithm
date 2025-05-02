#isPalindrome

s = input()

# if s[:len(s)] == s[::-1]:
#   print(1)
# else:
#   print(0)

print(1 if s == s[::-1] else 0)