import sys

N,M = map(int,sys.stdin.readline().split())
min_list = []
table = []

for _ in range(N):
    row = list(sys.stdin.readline().strip())
    table.append(row)


for i in range(N-7):
    for j in range(M-7):
        W = 0
        B = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                    if table[x][y]!='W':
                        W += 1
                    if table[x][y]!='B':
                        B += 1
                else:
                    if table[x][y]!='B':
                        W += 1
                    if table[x][y]!='W':
                        B += 1
        min_list.append(min(W,B))

print(min(min_list))