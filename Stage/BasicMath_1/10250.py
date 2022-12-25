import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    H,W,N = map(int,sys.stdin.readline().rstrip().split())
    if(N%H==0):
        room = H*100+(N//H)
    else:
        room = (N%H)*100+(N//H+1)
    print(room)