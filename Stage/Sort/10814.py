import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    num, name = sys.stdin.readline().split()
    data.append((int(num),name))


data.sort(key=lambda x:x[0])

for i in data:
    print(*i)