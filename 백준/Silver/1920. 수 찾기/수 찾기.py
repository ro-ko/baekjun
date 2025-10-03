import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for i in check:
    if i in data:
        print(1)
    else:
        print(0)