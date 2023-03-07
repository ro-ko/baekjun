import sys

N, M = map(int, sys.stdin.readline().strip().split())

mat1 = []
mat2 = []

for T in range(N):
    mat1.append(list(map(int, sys.stdin.readline().strip().split())))
for T in range(N):
    mat2.append(list(map(int, sys.stdin.readline().strip().split())))
    
sum = [[x+y for x,y in zip(a,b)] for a,b in zip(mat1,mat2)]

for arr in sum:
    print(*arr)