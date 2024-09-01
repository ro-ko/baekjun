import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
data = sorted(set(num))

table = {}
for i, n in enumerate(data):
    table[n]=i

ret = []
for i in range(N):
    ret.append(table[num[i]])

print(*ret)

"""
arr = list(map(int, stdin.read().split()))
dic = {x: i for i, x in enumerate(sorted(set(arr)))}
print(' '.join(map(str, [dic[x] for x in arr])))
"""