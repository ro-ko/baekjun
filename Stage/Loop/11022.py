import sys

T = int(sys.stdin.readline())

for i in range(1,T+1):
    num = list(map(int, sys.stdin.readline().split()))
    print(f"Case #{i}: {num[0]} + {num[1]} = {num[0]+num[1]}")