import sys
input = sys.stdin.readline

num = int(input())
divisors = list(map(int, input().split()))
divisors.sort()
print(divisors[0]*divisors[-1])