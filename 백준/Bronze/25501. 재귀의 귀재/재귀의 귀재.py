import sys
input = sys.stdin.readline

def recursion(s, l, r, t):
    t += 1
    if l >= r: return (1, t)
    elif s[l] != s[r]: return (0, t)
    else: return recursion(s, l+1, r-1, t)

def isPalindrome(s):
    time = 0
    return recursion(s, 0, len(s)-1, time)

n = int(input())

for _ in range(n):
    val = input().strip()
    print(*isPalindrome(val))