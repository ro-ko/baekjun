import sys

input = sys.stdin.readline().rstrip()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in croatia:
    input = input.replace(i, '@')
print(len(input))