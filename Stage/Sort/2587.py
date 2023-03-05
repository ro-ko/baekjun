import sys

arr = []
for _ in range(5):
    n = int(sys.stdin.readline().strip())
    arr.append(n)

arr.sort()
print(int(sum(arr)/5),arr[2],sep='\n')