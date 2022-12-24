import sys

T = int(sys.stdin.readline())

arr = []
for i in range(T):
    arr.append(list(sys.stdin.readline().rstrip()))

for i in range(T):
    score = 0
    correct = False
    suc = 0
    for j in range(len(arr[i])):
        if(arr[i][j]=='O')&(correct==False):
            suc = 1
            score += suc
            correct = True
        elif(arr[i][j]=='O')&(correct==True):
            suc += 1
            score += suc
        else:
            correct = False
            suc = 0
    print(score)