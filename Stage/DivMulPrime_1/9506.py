import sys
from math import sqrt


while(True):
    n = int(sys.stdin.readline().strip())
    if n==-1:
        break
    div = [1]
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            div.extend({i,n//i})
    if n == sum(div):
        div.sort()
        print(n,'=',end=' ')
        print(*div,sep=' + ')
    else:
        print(f'{n} is NOT perfect.')