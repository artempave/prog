from typing import List, Tuple

def min_edge(G: List[Tuple[int, int, int]], Q) -> Tuple[int, int, int]:
    min_e: Tuple[int, int, int] = None
    u: int
    v: int
    l: int
    for e in G:
        u, v, l = e
        if ((u in Q) and (v not in Q)) or ((v in Q) and (u not in Q)):
            if (min_e == None) or (l < min_e[2]):
                min_e = e
    return min_e

def Prim_MST(G: List[Tuple[int, int, int]], N: int):
    # создаем пустой список для хранения ребер остова
    A: List[Tuple[int, int]] = []
    # создаем список для покрытых вершин и кладем в него любую вершину
    Q: List[int] = [0]
    # перебираем ребра, можно запустить "вечный" цикл и завершить его с помощью break,
    # который вызовется, когда min_edge вернет None
    s: int = 0
    while True:
        e: Tuple[int, int] = min_edge(G, Q)
        if e == None:
            break
        s += e[2]
        A.append((e[0], e[1]))
        if e[1] in Q:
            Q.append(e[0])
        else:
            Q.append(e[1])
    print(s)
    # возвращаем остов
    return A

# функция печати остова в нужном формате (печатает в том числе и размер остова)
def print_spanning_tree(A: List[Tuple[int, int]]) -> None:
    for edge in A:
        print(f"({edge[0]}, {edge[1]})", end = " ")



# считываем первую строку
N: int = int(input())

edges: List[Tuple[int, int, int]]= []
# считываем ребра
while True:
    try:
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    except EOFError:
        break

# делаем работу и печатаем результат
A: Tuple[int, int] = Prim_MST(edges, N)
print_spanning_tree(A)