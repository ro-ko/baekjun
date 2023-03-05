import sys
from math import sqrt

div = []
N, K = map(int, sys.stdin.readline().strip().split())

for i in range(1, int(sqrt(N))+1):
    if N%i == 0:
        if i*i==N:
            div.append(i)
        else:
            div.append(i)
            div.append(N//i)

div.sort()
if len(div)<K:
    print(0)
else:
    print(div[K-1])