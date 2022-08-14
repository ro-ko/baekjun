from math import sqrt

num = list(map(int,input().split()))

for i in range(num[0],num[1]+1):
    prime =True
    for j in range(2, int(sqrt(i))+1):
        if i%j==0:
            prime = False
            break
    if prime==True:
        print(i)
    else: continue