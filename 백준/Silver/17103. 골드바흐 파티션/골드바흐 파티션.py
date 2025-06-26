import sys

arr = [1 for _ in range(1000001)]
arr [0] = arr[1] = 0

for i in range(2, 100001):
    if arr[i] == 1:
        for j in range(i*2, 1000001, i):
            arr[j] = 0

def check_prime(n):
    cnt = 0
    for i in range(2, (n//2)+1):
        if arr[i] == 1 and arr[n-i] == 1:
            cnt += 1

    return cnt

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N =int(sys.stdin.readline().strip())
    print(check_prime(N))