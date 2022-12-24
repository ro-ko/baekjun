Num = set(range(1,10001))
D = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    if(i<10001):
        D.add(i)

self_Num = sorted(Num - D)
for i in self_Num:
    print(i)