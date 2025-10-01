from collections import deque
n = int(input())
qslist = list(map(int, input().split()))
vallist = list(map(int,input().split()))
m = int(input())
inputList = list(map(int,input().split()))

queue = deque()
for i in range(len(qslist)-1,-1,-1):
    if qslist[i] == 0:
        queue.append(vallist[i])
for i in range(m):
    queue.append(inputList[i])
for i in range(m):
    print(queue[i], end=" ")