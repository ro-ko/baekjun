import sys
from math import sqrt

def is_prime(x:int)->bool:
    if x==1:
        return False
    else:
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                return False
        return True
        
T  = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())

    a, b = n//2, n//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
