
def solution(s, n):
    answer = ''
    for ch in s:
        if ch.isupper():
            base = ord('A')
        elif ch.islower():
            base = ord('a')
        else:
            answer += ch
            continue
            
        num = (ord(ch) - base + n) % 26
        answer += chr(num + base)
    return answer