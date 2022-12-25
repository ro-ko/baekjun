import sys

s = int(sys.stdin.readline().rstrip())

num = 0
while(1):
    if(s%5==0):
        num += (s//5)
        print(num)
        break
    num += 1
    s -= 3
    if(s<0):
        print(-1)
        break