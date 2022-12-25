import sys

input = list(map(int, sys.stdin.readline().split()))

if(input[2]-input[1]<=0): print(-1)
else:
    print(input[0]//(input[2]-input[1])+1)