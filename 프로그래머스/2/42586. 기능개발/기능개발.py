'''
0번째 기능이 100찍을때까지 time ++
100이면 pop시키고 cnt ++
'''
def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    
    while len(speeds) > 0:
        if progresses[0] + time*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)
    return answer