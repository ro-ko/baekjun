import sys

input = int(sys.stdin.readline().rstrip())
input -= 1

num = 1
while(1):
    if (3*num*(num-1))>=input:
        break
    num += 1
print(num)