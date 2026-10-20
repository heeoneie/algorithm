def solution(answers):
    answer = []
    d = {1: 0, 2: 0, 3: 0}
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(0, len(answers)):
        if one[i % len(one)] == answers[i]:
            d[1] += 1
        if two[i % len(two)] == answers[i]:
            d[2] += 1
        if three[i % len(three)] == answers[i]:
            d[3] += 1
            
    max_num = max(d.values())
    for name, cnt in d.items():
        if max_num <= cnt:
            answer.append(name)
    return answer