def solution(s):
    if s[0] == ')':
        return False
    
    temp = []
    for char in s:
        if char == '(':
            temp.append(char)
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    return len(temp) == 0