import sys

N = int(sys.stdin.readline())

dance = ["ChongChong"]

for _ in range(N):
    a, b = sys.stdin.readline().split()
    if a not in dance and b not in dance:
        continue
    else:
        dance.append(a)
        dance.append(b)

print(len(set(dance)))