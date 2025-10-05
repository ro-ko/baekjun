def m2s(t):
    m, s = map(int, t.split(":"))
    return m*60+s

def s2m(t):
    m, s = t//60, t%60
    ret = f"{m:02}:{s:02}"
    return ret

def solution(video_len, pos, op_start, op_end, commands):
    video_len = m2s(video_len)
    op_start = m2s(op_start)
    op_end= m2s(op_end)
    pos = m2s(pos)
    
    for action in commands:
        if op_start <= pos < op_end:
            pos = op_end
        if action == "next":
            if video_len < pos + 10:
                pos = video_len
            else:
                pos += 10
        elif action == "prev":
            if pos < 10:
                pos = 0
            else:
                pos -= 10
    if op_start <= pos < op_end:
            pos = op_end
    answer = s2m(pos)
    
    return answer