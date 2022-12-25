import sys

input = list(sys.stdin.readline().rstrip().split())

sangsu = []

for i in range(len(input)):
    num = input[i][::-1]
    sangsu.append(int(num))
    
print(max(sangsu))