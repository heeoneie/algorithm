while True:
    string = input()
    if string == '.':
        break
    stack = []
    for val in string:
        if val == '(' or val == '[':
            stack.append(val)
        elif val == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(val)
                break
        elif val == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(val)
                break
    if stack:
        print("no")
    else:
        print("yes")