

def solution(wallet, bill):
    answer = 0    

    wallet_x, wallet_y = sorted(wallet)
    bill_x, bill_y = sorted(bill)
    
    while True:
        if (wallet_x<bill_x) or (wallet_y<bill_y):
            bill_y = bill_y//2
            answer += 1
            bill_x, bill_y = sorted([bill_x, bill_y])
        else:
            break
            
    
    return answer