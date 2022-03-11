#1 ≤ N ≤ 1,000,000

X = int(input())
sum = 0
for i in range(1,X+1):
    sum += i*(X//i)
print(sum)