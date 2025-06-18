import sys

N, M = map(int, sys.stdin.readline().split())

poketmon_dict = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    poketmon_dict[name] = i + 1
    poketmon_dict[i + 1] = name

for _ in range(M):
    input = sys.stdin.readline().strip()
    if input.isdigit():
        print(poketmon_dict[int(input)])
    else:
        print(poketmon_dict[input])
