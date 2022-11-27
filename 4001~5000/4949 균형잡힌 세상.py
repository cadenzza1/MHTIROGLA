strings = input().split('.')

for string in strings:
    stack = []
    for i in string:
        if i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                print("NO")
                break
        elif i == '(':
            stack.append('(')
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                print("NO")
                break
        elif i == '[':
            stack.append('[')
    else:
        if stack:
            print("NO")
        else:
            print("YES")