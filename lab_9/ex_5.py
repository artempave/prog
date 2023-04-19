ansver = []


def graph_list(edges, tree):
    gr_list = [[] for _ in range(max(tree) + 1)]
    for edge in edges:
        gr_list[edge[0]].append(edge[1])
        gr_list[edge[1]].append(edge[0])
    return gr_list


def prefix(gr_list, root, brooken=[]):
    global ansver
    brooken.append(root)
    mas = gr_list[root]
    if len(mas) < 1:
        return
    ansver.append(root)
    for i in mas:
        if i not in brooken:
            prefix(gr_list, i, brooken)


def postfix(gr_list, root, brooken=[]):
    global ansver
    brooken.append(root)
    mas = gr_list[root]
    if len(mas) < 1:
        return
    for i in mas:
        if i not in brooken:
            postfix(gr_list, i, brooken)
    ansver.append(root)


def built(root, E):
    tree = []
    for x, y in E:
        if x not in tree:
            tree.append(x)
        if y not in tree:
            tree.append(y)
    return tree


root = int(input())
edges = []
while True:
    try:
        edge = list(map(int, input().split()))
        edges.append(edge)
    except EOFError:
        break
G = graph_list(edges, built(root, edges))
prefix(G, root)
print(" ".join(map(str, ansver)))
ansver = []
postfix(G, root)
print(" ".join(map(str, ansver)))