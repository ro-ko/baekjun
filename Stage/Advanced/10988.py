import sys

string = sys.stdin.readline().strip()
Rstring = string[::-1]

print(int(string==string[::-1]))