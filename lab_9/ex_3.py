def graph_list(N, edges):
    gr_list = [set({}) for _ in range(N)]
    for edge in edges:
        gr_list[edge[0]].add(edge[1])
        gr_list[edge[1]].add(edge[0])
    for i in range(N):
        gr_list[i] = list(gr_list[i])
        gr_list[i].sort()
    return gr_list


def print_graph(gr_list):
    for n in gr_list:
        if n == []:
            print()
        else:
            print(" ".join(map(str, n)))


N = int(input())
edges = []
while True:
    try:
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    except EOFError:
        break
print_graph(graph_list(N, edges))


