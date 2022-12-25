import sys

input = int(sys.stdin.readline().rstrip())

num = 1
while(1):
    if (num*(num+1)/2)>=input:
        break
    num += 1
k = int(input-num*(num-1)/2)
if(num%2==0):
    print(f"{k}/{num+1-k}")
else:
    print(f"{num+1-k}/{k}")