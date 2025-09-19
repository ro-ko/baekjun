import sys

from collections import deque


queue = deque()
ret = []

N = int(sys.stdin.readline())
M = map(int, sys.stdin.readline().split())

# 양수 오른쪽 , 음수 왼쪽
for idx, K in enumerate(M):
    queue.append((idx + 1, K))

ret = []
while len(queue) > 1:
    idx, K = queue.popleft()
    ret.append(idx)
    if K > 0:
        for _ in range(K-1):
            queue.append(queue.popleft())
    else:
        for _ in range(0, K, -1):
            queue.appendleft(queue.pop())

ret.append(queue.popleft()[0])
print(" ".join(map(str, ret)))