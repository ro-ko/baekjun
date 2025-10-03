import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

ret = ""
for idx, c in enumerate(arr[0]):
    flag = True
    for dir in arr:
        if c != dir[idx]:
            flag = False
            ret += "?"
            break
    if flag:
        ret += c

print(ret)