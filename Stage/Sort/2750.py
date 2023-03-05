import sys

N = int(sys.stdin.readline().strip())

arr = []
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    arr.append(n)
    
arr.sort()
for x in arr:
    print(x)