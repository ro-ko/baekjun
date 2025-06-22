import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

lcm = B * M // gcd(B, M)

up = (A * lcm // B) + (N * lcm // M)
down = lcm

Gcd = gcd(up, down)
print(up//Gcd, down // Gcd)