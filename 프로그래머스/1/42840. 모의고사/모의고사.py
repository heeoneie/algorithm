'''
수포자1 패턴: 1 2 3 4 5
수포자2 패턴: 2 1 2 3 2 4 2 5
수포자3 패턴: 3 3 1 1 2 2 4 4 5 5
* 1만하고 받은 문제 루핑돌려서 맞은 갯수 세서 많이 맞은 사람 출력
'''
def solution(answers):
    answer = []
    a = [1,2,3,4,5] * 10000
    b = [2,1,2,3,2,4,2,5] * 10000 
    c = [3,3,1,1,2,2,4,4,5,5] * 10000
    res = 0
    temp = []
    
    for i in range(len(answers)):
        if a[i] == answers[i]:
            res += 1
    temp.append(res)
    res = 0
    
    for i in range(len(answers)):
        if b[i] == answers[i]:
            res += 1
    temp.append(res)
    res = 0
    
    for i in range(len(answers)):
        if c[i] == answers[i]:
            res += 1
    temp.append(res)
    
    if temp.count(max(temp)) > 1:
        for i in range(len(temp)):
            if temp[i] == max(temp):
                answer.append(i+1)
    else:
        answer.append(temp.index(max(temp))+1)
        
    return answer