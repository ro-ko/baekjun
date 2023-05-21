import sys

x, y, z = map(int, sys.stdin.readline().split())
sum = x+y+z

if 2*max(x,y,z)<sum:
    print(sum)
else:
    print(2*(sum-max(x,y,z))-1)