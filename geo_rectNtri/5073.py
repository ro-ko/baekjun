import sys


while(True):
    length = list(map(int, sys.stdin.readline().split()))
    num = len(set(length))
    
    if length[0]==0:
        break
    elif 2*max(length)>=sum(length):
        print("Invalid")
    elif num==1:
        print("Equilateral")
    elif num==2:
        print("Isosceles")
    else:
        print("Scalene")
