import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    name, stat = sys.stdin.readline().strip().split()
    if stat=="enter":
        arr.append(name)
    elif stat=="leave":
        arr.remove(name)
arr.sort(reverse=True)

print(*arr, sep='\n')