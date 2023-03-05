import sys
from math import sqrt

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

def is_prime(x:int)->bool:
    if x==1:
        return False
    else:
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                return False
        return True
        
prime = []
for num in range(M,N+1):
    if is_prime(num):
        prime.append(num)

prime.sort()
if len(prime)==0:
    print(-1)
else:
    print(sum(prime),prime[0],sep='\n')