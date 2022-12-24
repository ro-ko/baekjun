import sys

Set = set()
for i in range(10):
    Set.add(int(sys.stdin.readline())%42)

print(len(Set))