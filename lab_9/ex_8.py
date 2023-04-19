class Node:
    def __init__(self, x=None):
        self.name = x
        self.left_sun = None
        self.right_sun = None

    def __str__(self):
        return str(self.name)


def shunting_yard(string):
    stack = []
    queue = []
    prioretet = {"+": 0, "-": 0, "*": 1, "/": 1, "**": 2}
    operation = ["+", "-", "*", "/", "**"]
    if string[-1] in operation:
        return "error"
    l = len(string)
    for i in range(l):
        element = string[i]
        if element.isdigit():
            queue = calculate_ops(queue, element)
        elif element == "(":
            stack.append(element)
        elif element == ")":
            x = stack.pop()
            while x != "(":
                queue = calculate_ops(queue, x)
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
                    queue = calculate_ops(queue, x)
                stack.append(element)
        else:
            return "error"
    while stack != []:
        x = stack.pop()
        if x == "(":
            return "error"
        queue = calculate_ops(queue, x)
    if len(queue) != 1:
        return "error"
    return queue[0]


def calculate_ops(queue, element):
    stack = list(queue)
    operetion = ["*", "/", "+", "-", "**"]
    if element.isdigit():
        tree_Node = Node(element)
        stack.append(tree_Node)
    if element in operetion:
        tree_Node = Node(element)
        if len(stack) < 2:
            return "error"
        x = stack.pop()
        y = stack.pop()
        tree_Node.left_sun = y
        tree_Node.right_sun = x
        stack.append(tree_Node)
    return list(stack)


def print_tree(tree, flag=None):
    print("(", end="")
    if tree == None:
        if flag == 1:
            print(")", end=" ")
        else:
            print(")", end="")
        return
    print(tree, end=" ")
    print_tree(tree.left_sun, 1)
    print_tree(tree.right_sun, 0)
    if flag == 1:
        print(")", end=" ")
    else:
        print(")", end="")


string = input().split()
print_tree(shunting_yard(string))




