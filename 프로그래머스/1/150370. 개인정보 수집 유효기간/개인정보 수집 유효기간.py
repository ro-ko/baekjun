# 약관 A~Z
# 유효기간 1~100
#

def solution(today, terms, privacies):
    answer = []
    terms = {x.split()[0]:x.split()[1] for x in terms}
    privacies = [x.split() for x in privacies]
    
    t_y, t_m, t_d = map(int, today.split("."))
    t_y -= 2000
    t_value = t_y*28*12 + t_m*28 + t_d
    
    def check(info):
        y, m ,d = map(int, info[0].split("."))
        y -= 2000
        value = y*28*12 + m*28 + d
        dur = int(terms[info[1]])*28

        if value + dur <= t_value:
            return False
        else:
            return True
        

    for idx, info in enumerate(privacies):
        if not check(info):
            answer.append(idx+1)

    return answer