import sys

while(1):
    try:
        num = list(map(int, sys.stdin.readline().split()))
        print(num[0]+num[1])
    except: break