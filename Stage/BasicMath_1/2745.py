import sys

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N,B = sys.stdin.readline().strip().split()
sum = 0

l = list(N)
B = int(B)

for i in range(len(l)):
        sum += num.index(l[i])*(B**(len(l)-i-1))

print(sum)