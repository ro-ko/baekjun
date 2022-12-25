import sys

T = int(sys.stdin.readline().rstrip())
num = list(sys.stdin.readline().rstrip())

sum = 0
for i in num:
    sum += int(i)

print(sum)