def solution(clothes):
    answer = 1
    d = {}
    for c in clothes:
        if c[1] in d:
            d[c[1]] += 1
        else:
            d[c[1]] = 1
            
    for cnt in d.values():
        answer *= cnt + 1
    answer -= 1
    return answer