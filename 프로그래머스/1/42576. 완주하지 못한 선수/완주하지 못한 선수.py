def solution(participant, completion):
    answer = ''
    d = {}
    for p in participant:
        if p in d:
            d[p] += 1
        else:
            d[p] = 1
            
    for c in completion:
        if c in d:
            d[c] -= 1
            
    for name, cnt in d.items():
        if cnt != 0:
            answer += name
    return answer