def cnt(n):
    cnt = 0
    if(n<100):
        cnt = n
        return cnt
    else:
        cnt = 99
        for i in range(100,n+1):
            if(2*int(str(i)[1]) == int(str(i)[0])+int(str(i)[2])):
                cnt += 1
        return cnt
    
import sys

n = int(sys.stdin.readline())
print(cnt(n))