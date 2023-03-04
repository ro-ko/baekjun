import sys

N, M = map(int, sys.stdin.readline().strip().split())

arr = [*range(1,N+1)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x-1:y] = arr[x-1:y][::-1]

    
print(*arr)
