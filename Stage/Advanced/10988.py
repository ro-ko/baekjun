import sys

string = sys.stdin.readline().strip()

print(int(string==string[::-1]))