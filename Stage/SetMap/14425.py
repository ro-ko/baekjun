import sys

N, M = map(int,sys.stdin.readline().split())

S = []
test = []
for _ in range(N):
    S.append(sys.stdin.readline().strip())

for _ in range(M):
    test.append(sys.stdin.readline().strip())

cnt = 0
for s in test:
    if s in S:
        cnt += 1

print(cnt)

"""
import os
n,_,*s=os.read(0,os.fstat(0).st_size).split()
print(sum(map(set(s[:int(n)]).__contains__,s[int(n):])))
"""