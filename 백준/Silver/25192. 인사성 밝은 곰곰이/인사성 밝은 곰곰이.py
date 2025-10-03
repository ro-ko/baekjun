import sys

N = int(sys.stdin.readline())

enter = 0
ret = 0

arr = []
for _ in range(N):
    name = sys.stdin.readline().strip()
    if name == "ENTER":
        if (enter%2) == 0:
            ret += len(set(arr))
            arr = []
    else:
        arr.append(name)

ret += len(set(arr))

print(ret)