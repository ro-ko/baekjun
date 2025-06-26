import sys

N = int(sys.stdin.readline().strip())

ret = 0
num = 0
while True:
    num += 1
    if num*num <= N:
        ret += 1
    elif num*num > N:
        break

print(ret)