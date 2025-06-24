import sys

arr = [1 for _ in range(123456*2+1)]
for i in range(2, 123456*2):
    if arr[i]:
        for j in range(i*2, 123456*2+1, i):
            arr[j] = 0

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(sum(arr[n+1:2*n+1]))
