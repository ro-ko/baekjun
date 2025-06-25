def countdown(n):
    if n<=0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(n, 0, -1):
            print(i)

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
countdown(0)
countdown(10)