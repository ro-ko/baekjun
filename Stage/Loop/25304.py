sum = int(input())
real = 0

num = int(input())

for i in range(num):
    item = list(map(int, input().split()))
    real += item[0]*item[1]

if(real==sum): print("Yes")
else: print("No")