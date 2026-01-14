s = input().strip()

rm1 = s.count('1') // 2
rm0 = s.count('0') // 2

res = []

# 1: 앞에서 제거
for ch in s:
    if ch == '1' and rm1 > 0:
        rm1 -= 1
    else:
        res.append(ch)

# 0: 뒤에서 제거
final = []
for ch in reversed(res):
    if ch == '0' and rm0 > 0:
        rm0 -= 1
    else:
        final.append(ch)

print(''.join(reversed(final)))
