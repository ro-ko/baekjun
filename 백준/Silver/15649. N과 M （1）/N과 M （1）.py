import sys

input = sys.stdin.readline



n, m = map(int, input().split())

used = [False] * (n + 1)
result = []

def backtrack():
    if len(result) == m:
        print(*result)
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            result.append(i)
            backtrack()
            result.pop()
            used[i] = False

backtrack()
