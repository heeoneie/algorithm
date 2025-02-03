def changeSec(time):
    min, sec = map(int, time.split(':'))
    return 60 * min + sec

def solution(video_len, pos, op_start, op_end, commands):
    pos_sec = changeSec(pos)
    op_start_sec = changeSec(op_start)
    op_end_sec = changeSec(op_end)
    video_sec = changeSec(video_len)
    
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
        
    for command in commands:
        if command == 'prev':
            pos_sec -= 10
        else:
            pos_sec += 10
        if pos_sec < 0:
            pos_sec = 0
        elif pos_sec > video_sec:
            pos_sec = video_sec
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
    return f"{str(pos_sec//60).zfill(2)}:{str(pos_sec%60).zfill(2)}"