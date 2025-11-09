import sys

input = sys.stdin.readline

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 1e9

a_list.sort()
b_list.sort(reverse=True)

print(sum(a*b for a, b in zip(a_list, b_list)))
