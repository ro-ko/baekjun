import sys

table = []
M = -1
idx = (0, 0)
for i in range(9):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
    if M < max(table[i]):
        M = max(table[i])
        idx = (i+1, table[i].index(max(table[i]))+1)

print(M)
print(*idx)