def solution(s):
    answer = []
    for c in s:
        if c == '(':
            answer.append('(')
        else:
            if len(answer) <= 0:
                return False
            answer.pop(-1)
    if len(answer) > 0:
        return False
    else:
        return True