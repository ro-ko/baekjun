import sys

T = int(sys.stdin.readline().strip())

C = []
for i in range(T):
    m = int(sys.stdin.readline().strip())
    ret = []

    ret.append(m // 25)
    m = m%25
    ret.append(m // 10)
    m = m%10
    ret.append(m // 5)
    m = m%5
    ret.append(m)
    C.append(ret)

for x in C:
    print(*x)