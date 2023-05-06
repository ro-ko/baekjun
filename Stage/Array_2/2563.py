import sys

paper = [[0 for i in range(100)] for j in range(100)]

n = int(sys.stdin.readline().strip())

for i in range(n):
    x,y = map(int, sys.stdin.readline().strip().split())
    for j in range(10):
        for k in range(10):
            paper[j+x][k+y] = 1

ret = 0
for i in range(len(paper)):
    ret += sum(paper[i])

print(ret)