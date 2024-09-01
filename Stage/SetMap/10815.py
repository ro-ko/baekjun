import sys

def binary_search(target:int,arr:list)->int:
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 1
        elif arr[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return 0

N = int(sys.stdin.readline())
table = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
input = list(map(int,sys.stdin.readline().split()))

table.sort()
print(*[binary_search(x, table) for x in input])