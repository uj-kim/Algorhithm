import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
arr_a = set(map(int, input().split()))
arr_b = set(map(int, input().split()))

print(len(arr_a - arr_b))
print(*sorted(list(arr_a - arr_b)))