import sys

N, k = map(int, sys.stdin.readline().strip().split())

arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort(reverse=True)

print(arr[k-1])