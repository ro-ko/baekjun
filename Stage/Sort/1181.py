import sys

N = int(sys.stdin.readline())

lang = set()
for _ in range(N):
    string = sys.stdin.readline().strip()
    lang.add((len(string), string))

lang = sorted(lang)

for i in lang:
    print(i[1])