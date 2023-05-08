import sys

N = int(sys.stdin.readline().strip())

flag = False
for i in range(1, N+1):
    if(N==i+sum(list(map(int,str(i))))):
        print(i)
        flag = True
        break
if(flag==False):
    print(0)