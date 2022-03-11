#(1 ≤ T ≤ 100,000)

T = int(input())

for i in range(T):
    num = int(input())
    sum = 0
    for j in range(1 ,num+1):
        sum += j * (num // j)
    print(sum)