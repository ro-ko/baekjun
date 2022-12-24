import sys

arr = []

for i in range(9):
    arr.append(int(sys.stdin.readline()))

print(max(arr), arr.index(max(arr))+1)