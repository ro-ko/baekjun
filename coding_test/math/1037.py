#2<=N<=1000000

num = int(input())
divisor = input().split()
divisor = [int(i) for i in divisor]

min = min(divisor)
max = max(divisor)

print(min*max)
