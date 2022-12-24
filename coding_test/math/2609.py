
num = input().split()
num = list(map(int,num))
#num = [int(i) for i in num]

a = num[0]
b = num[1]
c = 1
x = a * b

#euclidean algorithm
while True:
    c = a % b
    if c==0:
        break
    a = b
    b = c
print(b)
print(x//b)