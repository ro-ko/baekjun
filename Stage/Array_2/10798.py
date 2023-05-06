import sys

input = [sys.stdin.readline().strip() for i in range(5)]


for j in range(15):
    for i in range(5):
        if(j<len(input[i])):
            print(input[i][j], end='')