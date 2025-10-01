import sys

n, m = map(int, sys.stdin.readline().split())

result = 1
for i in range(n-m+1, n+1):
    result *= i
for i in range(1, m+1):
    result /= i
print(int(result))