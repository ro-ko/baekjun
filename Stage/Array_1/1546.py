import sys

T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(sum(arr)/T/max(arr)*100)