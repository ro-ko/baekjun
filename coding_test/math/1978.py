# num<=100
from math import sqrt

num = int(input())
num = 0
nums = list(map(int,input().split()))
for i in nums:
    if i==1:
        num += 1
        continue
    for j in range(2, int(sqrt(i))+1):
        if i%j==0:
            num += 1
            break
print(len(nums)-num)