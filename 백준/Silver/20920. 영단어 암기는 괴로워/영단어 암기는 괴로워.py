import sys


n, m = map(int, sys.stdin.readline().split())

data = {}
for _ in range(n):
    word = sys.stdin.readline().strip()

    if len(word)>=m:
        if word not in data:
            data[word] = 0
        else: data[word] += 1

ret = list(data.keys())
ret.sort(key=lambda x:(-data[x], -len(x), x))
print(*ret, sep="\n")
