import sys

input = list(sys.stdin.readline().rstrip())

alphabet = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

time = 0
for i in input:
    for j in alphabet:
        if i in j:
            time += alphabet.index(j) + 3
    
print(time)
