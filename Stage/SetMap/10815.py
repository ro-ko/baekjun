import sys

N = int(sys.stdin.readline())
table = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

print(*[int(x in table) for x in arr])