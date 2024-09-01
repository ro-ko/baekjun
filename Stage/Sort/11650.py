import sys

N = int(sys.stdin.readline())

point = []
for _ in range(N):
    point.append(tuple(map(int,sys.stdin.readline().strip().split())))

point.sort()
for i in range(N):
    print(*point[i])