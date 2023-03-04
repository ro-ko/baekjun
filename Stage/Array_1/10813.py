import sys

N, M = map(int, sys.stdin.readline().strip().split())

arr = [x+1 for x in range(N)]

for i in range(M):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
    
print(*arr)