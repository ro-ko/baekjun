import sys

num = int(sys.stdin.readline().strip())
string = 'int'

for i in range(num//4):
    string = 'long ' + string
    
print(string)