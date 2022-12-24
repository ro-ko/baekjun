import sys

input = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))
ans = [i for i in arr if i<input[1]]
print(*ans)