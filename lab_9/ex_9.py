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


def tree_H(tree):
    if tree == None:
        return 0
    left_H = tree_H(tree.left_sun)
    right_H = tree_H(tree.right_sun)
    return max(left_H, right_H) + 1


def do_matrix(H):
    matrix = [[" "] * (2 ** H - 1) for _ in range(3 * H)]
    return matrix


def print_tree(tree):
    H = tree_H(tree)
    j = 2 ** H - 1
    matrix = do_matrix(H)
    matrix[0][0] = "."
    tree_rec(matrix, tree, 0, j // 2, H)
    for i in matrix:
        print("".join(i).rstrip())


def tree_rec(matrix, tree, i, j, H):
    if tree == None:
        return
    matrix[i][j] = tree.name
    if tree.left_sun:
        matrix[i + 1][j] = "|"
        for j1 in range(j - 2 ** (H - 2), j + 2 ** (H - 2) + 1):
            matrix[i + 2][j1] = "-"
        tree_rec(matrix, tree.left_sun, i + 3, j - 2 ** (H - 2), H - 1)
    if tree.right_sun:
        matrix[i + 1][j] = "|"
        for j1 in range(j - 2 ** (H - 2), j + 2 ** (H - 2) + 1):
            matrix[i + 2][j1] = "-"
        tree_rec(matrix, tree.right_sun, i + 3, j + 2 ** (H - 2), H - 1)


string = input().split()
tree = shunting_yard(string)
print_tree(tree)

