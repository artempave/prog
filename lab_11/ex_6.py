# функция принимает на вход количество вершин в графе N и список ребер edges
# каждое ребро задано кортежом (u, v, cost)
# вернуть функция должна списки смежных вершин в описанном в задании формате
from typing import List, Tuple

def edges2adj(N: int, edges: List[Tuple[int, int, int]]):
    grah_list: List[List[int]] = [[] for _ in range(N)]
    u: int
    v: int
    l: int
    for u, v, l in edges:
        grah_list[u].append((v, l))
        grah_list[v].append((u, l))
    for i in range(N):
        grah_list[i].sort()
    return grah_list


# принимает на вход граф G, построенный с помощью edges2adj, и массив предков
# находит сумму весов ребер, записанных в pi, печатает сумму и сам список pi
def print_spanning_tree(G: List[List[int]], pi: List[int]):
    l: int = len(pi)
    s: int = 0
    for i in range(l):
        if pi[i] != None:
            k: int = len(G[i])
            for j in range(k):
                if pi[i] == G[i][j][0]:
                    s += G[i][j][1]
    print(s)
    print(pi)



# считываем количество вершин
N = int(input())

# считываем массив предков pi (не забываем заменить -1 на None)
pi: List[int] = list(map(int, input().split()))
pi = [None if i == -1 else i for i in pi]

edges: List[Tuple[int, int, int]] = []
# считываем ребра
while True:
    try:
        edge: Tuple[int, int, int] = tuple(map(int, input().split()))
        edges.append(edge)
    except EOFError:
        break

# делаем работу и печатаем результат
G = edges2adj(N, edges)
print_spanning_tree(G, pi)