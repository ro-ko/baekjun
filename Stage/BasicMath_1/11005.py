import sys

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N,B = map(int, sys.stdin.readline().strip().split())

ans = ""

while(N!=0):
    ans += num[N%B]
    N = N // B

print(ans[::-1])