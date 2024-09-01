import sys

N = int(sys.stdin.readline())

point = []
for _ in range(N):
    a,b = map(int,sys.stdin.readline().strip().split())
    point.append([b,a])

point.sort()

for i in range(N):
    a,b = point[i]
    print(b,a)