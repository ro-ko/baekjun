import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

n = (n//100)*100

if n%m ==0:
    print("00")
else:
    ret = m-(n%m)
    print(f"0{ret}") if ret<10 else print(ret)