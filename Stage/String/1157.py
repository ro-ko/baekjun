import sys

string = sys.stdin.readline().rstrip()
string = string.upper()

alphabet = list(set(string))
cnt = []

for i in alphabet:
    cnt.append(string.count(i))

if (cnt.count(max(cnt)))>1:
    print('?')
else:
    print(alphabet[cnt.index(max(cnt))])