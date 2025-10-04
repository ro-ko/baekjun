import sys

input = sys.stdin.readline


def contour(l):
    if l == 0:
        return "-"
    
    arr = ""
    for c in contour(l-1):
        if c == "-":
            arr += "- -"
        else:
            arr += " "*3
    return arr

while True:
    n = input()
    if n == "":
        break
    n = int(n)
    print(contour(n))
    