def shunting_yard(string):
    stack = []
    queue = []
    prioretet = {"+":0, "-":0, "*":1, "/":1, "**":2}
    operation = ["+", "-", "*", "/", "**"]
    if string[-1] in operation:
        return "error"
    l = len(string)
    for i in range(l):
        element = string[i]
        if element.isdigit():
            queue.append(int(element))
        elif element == "(":
            stack.append(element)
        elif element == ")":
            x = stack.pop()
            while x != "(":
                queue.append(x)
                if stack == []:
                    return "error"
                x = stack.pop()
        elif element in operation:
            if string[i + 1] in operation:
                return "error"
            if stack == [] or stack[-1] == "(" or element == "**":
                stack.append(element)
            elif prioretet[stack[-1]] < prioretet[element]:
                stack.append(element)
            else:
                while stack and prioretet[stack[-1]] >= prioretet[element]:
                    x = stack.pop()
                    queue.append(x)
                stack.append(element)
        else:
            return "error"
    while stack != []:
        x = stack.pop()
        if x == "(":
            return "error"
        queue.append(x)
    return queue

string = input().split()
ansver = shunting_yard(string)
print(" ".join(map(str, ansver)))