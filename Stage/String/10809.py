import sys

name = list(sys.stdin.readline().rstrip())
arr = []

for i in range(ord("a"),ord("z")+1):
    if chr(i) in name:
        arr.append(name.index(chr(i)))
    else:
        arr.append(-1)
        
print(*arr)