import sys

while(True):
    A,B = map(int, sys.stdin.readline().strip().split())
    if A==0 & B==0:
        break
    if B%A==0:
        print('factor')
    elif A%B==0:
        print('multiple')
    else:
        print('neither')