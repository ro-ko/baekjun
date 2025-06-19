import sys

N = int(sys.stdin.readline().strip())

dict = {}

arr = list(map(int, sys.stdin.readline().strip().split()))
for num in arr:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

M = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

for num in arr:
    if num in dict:
        print(dict[num])
    else:
        print(0)