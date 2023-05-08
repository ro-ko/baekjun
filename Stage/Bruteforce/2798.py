import sys
import itertools

N, M = map(int, sys.stdin.readline().strip().split())
num = list(map(int, sys.stdin.readline().strip().split()))

com = itertools.combinations(num, 3)

max = -1
for x, y, z in com:
    if (x+y+z>max) & (x+y+z <= M):
        max = x+y+z

print(max)
