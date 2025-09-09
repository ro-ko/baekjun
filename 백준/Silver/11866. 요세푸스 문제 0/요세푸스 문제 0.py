import sys

from collections import deque


queue = deque()
ret = []

N, K = map(int, sys.stdin.readline().split())


for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 0:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    ret.append(queue.popleft())

print("<" + ", ".join(map(str, ret)) + ">")