#1<=n<=10000

x = 1
while x:
    x = input()
    if x=='':
        break
    else:
        x = int(x)
    ans = 1
    num = 0
    while True:
        num += 1
        if ans%x==0:
            print(num)
            break
        else:
            ans = 10*(ans%x)+1

