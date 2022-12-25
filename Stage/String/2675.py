import sys

T = int(sys.stdin.readline())

for i in range(T):
    arr = list(sys.stdin.readline().rstrip().split())
    output = ''
    for j in list(arr[1]):
        output += int(arr[0])*j
    print(output)