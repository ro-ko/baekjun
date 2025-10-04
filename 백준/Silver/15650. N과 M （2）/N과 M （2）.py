import sys

input = sys.stdin.readline



n, m = map(int, input().split())

num = [False for _ in range(n+1)]
ret = [0]

def back():
    if len(ret) == m+1:
            print(*ret[1:])
            return
    for i in range(1, n+1):
        if not num[i] and ret[-1]<i:
            ret.append(i)
            num[i] = True
            back()
            ret.pop()
            num[i] = False

back()