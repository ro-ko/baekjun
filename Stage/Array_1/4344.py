import sys

T = int(sys.stdin.readline())

arr = []

for i in range(T):
    arr.append(list(map(int, sys.stdin.readline().split()))[1:])

for i in range(T):
    avg = sum(arr[i])/len(arr[i])
    n = 0
    for j in arr[i]:
        if j>avg: n += 1
    print(f"{n/len(arr[i])*100:.3f}%")