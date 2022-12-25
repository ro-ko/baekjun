import sys

def removeDuplicate(string):
    prev = None
    ret = ''
    for i in string:
        if i != prev:
            ret += i
        prev = i
    return ret

T = int(sys.stdin.readline())

cnt = 0
for i in range(T):
    string = removeDuplicate(sys.stdin.readline().rstrip())
    arr = list(string)

    if len(arr)==len(set(arr)):
        cnt += 1

print(cnt)
