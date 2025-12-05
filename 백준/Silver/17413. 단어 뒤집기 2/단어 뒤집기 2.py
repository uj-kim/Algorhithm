s = input()
stack = []
result = ''
inside_tag = False

for c in s:
    if c == '<':
        # stack 안에 뒤집어야 할 문자들 먼저 비우고 출력
        while stack:
            result += stack.pop()
        inside_tag = True
        result += c

    elif c == '>':
        inside_tag = False
        result += c

    elif inside_tag:
        result += c

    else:
        if c == ' ':
            while stack:
                result += stack.pop()
            result += ' '
        else:
            stack.append(c)

while stack:
    result += stack.pop()

print(result)
