import sys

N = int(sys.stdin.readline())

x = []
y = []

for _ in range(N):
    Px, Py = map(int, sys.stdin.readline().split())
    x.append(Px)
    y.append(Py)

w = max(x)-min(x)
h = max(y)-min(y)

print(w*h)