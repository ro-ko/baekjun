while True:
    temp = input().rstrip()
    if temp == ".":
        break

    stack = []
    for i in temp:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break

    print("no" if stack else "yes")
