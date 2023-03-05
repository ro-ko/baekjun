import sys

N, M = map(int, sys.stdin.readline().strip().split())

arr = [*range(1,N+1)]

for _ in range(M):
    s, e, m = map(int, sys.stdin.readline().strip().split())
    arr[s-1:e] = arr[m-1:e]+arr[s-1:m-1]
print(*arr)

