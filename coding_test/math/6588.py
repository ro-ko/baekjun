from math import sqrt
x = 1
num = []
while x:
    x = int(input())
    if x==0:
        break
    num.append(x)

for i in num:
    primeNums = []
    for j in range (3,i+1,2):
        prime = True
        for k in range(2,int(sqrt(j))+1):
            if j%k==0:
                prime = False
                break
        if prime==True:
            primeNums.append(j)
    for p in primeNums:
        exist = False
        if i-p in primeNums:
            print('{} = {} + {}'.format(i,p,i-p))
            exist = True
            break
    if exist==False:
        print('Goldbach\'s conjecture is wrong.')
