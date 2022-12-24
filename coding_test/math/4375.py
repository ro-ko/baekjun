while True :
    try:
        x = int(input())
    except:
        break
    
    num = 0
    ans = 1
    while True:
        num = 10*num+1
        num %= x
        if num == 0:
            print(ans)
            break
        ans += 1