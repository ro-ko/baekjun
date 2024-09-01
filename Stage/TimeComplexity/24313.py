import sys

a1, a2 = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())
n0 = int(sys.stdin.readline().strip())

print(int((a1*n0+a2<=c*n0)&(a1<=c)))