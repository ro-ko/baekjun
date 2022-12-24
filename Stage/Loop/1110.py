import sys

num = int(sys.stdin.readline())
N = num

cycle = 1
while(1):
    N = (N%10)*10+(((N//10)+(N%10))%10)
    if(N == num): break
    cycle += 1

print(cycle)
