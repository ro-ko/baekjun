import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)