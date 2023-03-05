from math import sqrt

M ,N = map(int,input().split())

for num in range(M,N+1):
    if num == 1:
        continue
    prime =True
    for i in range(2, int(sqrt(num))+1):
        if num%i==0:
            prime = False
            break
    if prime==True:
        print(num)