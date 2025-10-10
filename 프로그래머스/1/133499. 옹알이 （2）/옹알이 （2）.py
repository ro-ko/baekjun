def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    
    
    def check(string):
        for pattern in speak:
            if pattern*2 not in string:
                string = string.replace(pattern, " ")
            
        if string.isspace():
            return True
        else:
            return False
    
    for x in babbling:
        if check(x):
            answer += 1
    return answer