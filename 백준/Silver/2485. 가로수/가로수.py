import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(sys.stdin.readline().strip())

num = [int(sys.stdin.readline().strip()) for _ in range(N)]
diff = [num[i+1] - num[i] for i in range(N - 1)]

GCD = diff[0]
for i in range(N - 1):
    TEMP = gcd(GCD, diff[i])
    if TEMP < GCD:
        GCD = TEMP

print((num[N-1]-num[0])//GCD - len(num) + 1)

