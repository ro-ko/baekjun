import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    
    f = [i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            f[j] += f[j-1]
    print(f[-1])