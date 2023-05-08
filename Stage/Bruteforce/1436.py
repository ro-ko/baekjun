import sys

N = int(sys.stdin.readline())

i = 666
count = 0

while True:
    if str(666) in str(i):
        count += 1
    if count == N:
        print(i)
        break
    i += 1
