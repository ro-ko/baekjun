import sys

table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

credit = 0
score = 0

for _ in range(20):
    subject, C, S = sys.stdin.readline().split()
    if S == 'P':
        continue
    credit += float(C)
    score += float(C) * table[S]
    
print(f"{score/credit:.6f}")
