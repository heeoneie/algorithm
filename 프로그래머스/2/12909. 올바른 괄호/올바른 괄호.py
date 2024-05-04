'''
s의 0번째가 (인지 체크 아니면 false
열린 괄호면 append하고 닫힌 괄호면 열린 괄호 있는 지 체크해서 없으면 false
있으면 열린 괄호 pop
stack에 원소가 남아 있다면 false
'''
def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else: 
            if stack == []:
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        return False
    return True