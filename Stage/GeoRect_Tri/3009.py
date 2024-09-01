import sys

x = list(map(int,sys.stdin.readline().split()))
y = list(map(int,sys.stdin.readline().split()))
z = list(map(int,sys.stdin.readline().split()))
d = []

if x[0]==y[0]:
    d.append(z[0])
elif x[0]==z[0]:
    d.append(y[0])
else:
    d.append(x[0])

if x[1]==y[1]:
    d.append(z[1])
elif x[1]==z[1]:
    d.append(y[1])
else:
    d.append(x[1])

print(*d)