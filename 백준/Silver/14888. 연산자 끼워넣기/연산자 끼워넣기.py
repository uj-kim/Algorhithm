import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
plus, minus, mul, divi = map(int, input().split())
cnt = [plus, minus, mul, divi] 

max_value = -10**18
min_value =  10**18

def apply(a, b, op_idx):
    if op_idx == 0:   
        return a + b
    elif op_idx == 1: 
        return a - b
    elif op_idx == 2: 
        return a * b
    else:             
        if a < 0:
            return - (abs(a) // b)
        return a // b

def dfs(i, cur):
    global max_value, min_value
    if i == n:
        if cur > max_value: max_value = cur
        if cur < min_value: min_value = cur
        return

    for op in range(4):
        if cnt[op] > 0:
            cnt[op] -= 1
            nxt = apply(cur, arr[i], op)
            dfs(i + 1, nxt)
            cnt[op] += 1

dfs(1, arr[0])
print(max_value)
print(min_value)
