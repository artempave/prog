from typing import List, Tuple
# принимает на вход граф G в виде списка ребер и множество вершин Q
# ребро - это tuple вида (u, v, cost)
def min_edge(G: List[Tuple[int, int, int]], Q) -> Tuple[int, int, int]:
    # инициализируем текущее минимальное ребро
    min_e: Tuple[int, int, int] = None
    u: int
    v: int
    l: int
    # перебираем все ребра и ищем минимальное, удовлетворяющее условиям
    # помните, что в Q может быть любой конец ребра!
    for e in G:
        u, v, l = e
        if ((u in Q) and (v not in Q)) or ((v in Q) and (u not in Q)):
            if (min_e == None) or (l < min_e[2]):
                min_e = e
    # возвращаем ответ
    return min_e


# считываем количество вершин
N: int = int(input())

# считываем вершины разреза
Q: Tuple[int, int] = tuple(map(int, input().split()))

edges:List[Tuple[int, int, int]] = []
# считываем ребра
while True:
    try:
        edge:Tuple[int, int, int] = tuple(map(int, input().split()))
        edges.append(edge)
    except EOFError:
        break

# делаем работу и печатаем результат
print(min_edge(edges, Q))
