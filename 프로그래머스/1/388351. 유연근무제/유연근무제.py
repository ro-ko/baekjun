def hTom(t):
    return (t // 100) * 60 + (t % 100)

def solution(schedules, timelogs, startday):
    answer = 0
    
    for man, time in zip(schedules, timelogs):
        flag = True
        for i, t in enumerate(time):
            if (i+startday)%7 in [0, 6]:
                continue
            if hTom(t) - hTom(man) > 10:
                flag = False
                break
        if flag:
            answer += 1
            
    return answer