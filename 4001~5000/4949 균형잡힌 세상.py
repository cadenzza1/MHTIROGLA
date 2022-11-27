strings = []
while True:
    string = input()
    if string == '.':
        break
    else:
        strings.append(string)

for string in strings:
    stack = []
    for i in string:
        if i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        elif i == '(':
            stack.append('(')
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        elif i == '[':
            stack.append('[')
    else:
        if stack:
            print("no")
        else:
            print("yes")