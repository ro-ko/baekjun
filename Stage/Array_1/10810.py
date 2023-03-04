import sys

N, M = map(int, sys.stdin.readline().strip().split())

array = [0 for x in range(N)]

for i in range(M):
    s,e,n = map(int, sys.stdin.readline().strip().split())
    array[s-1:e] = [n for x in range(e-s+1)]
    
print(*array)