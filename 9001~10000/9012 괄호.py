t = int(input())

for _ in range(t):
    stack = []
    paren = input()
    for i in paren:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")
