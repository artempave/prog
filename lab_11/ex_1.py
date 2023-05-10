from typing import List, Tuple

def edges2matrix(N: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    matrix: List[List[int]] = [[0]*N for _ in range(N)]
    for edge in edges:
        matrix[edge[0]][edge[1]] = 1
        matrix[edge[1]][edge[0]] = 1
    return matrix


def is_safe(G: List[List[int]], e: Tuple[int, int]) -> bool:
    # e - это tuple с ребром
    u, v = e
    # сохраняем ребро e и удаляем его из G
    savedEdgeValue: int = G[u][v]
    G[u][v] = 0
    G[v][u] = 0
    visited: List[bool] = [False] * len(G)
    q: List[int] = [u]
    visited[u] = True
    # запускаем обход из вершины u.
    # Если во время обхода встретилась v, то ВОЗВРАЩАЕМ в граф ребро e с помощью savedEdgeInfo
    # и выдаем отрицательный результат
    while q:
        elem: int = q.pop(0)
        if elem == v:
            G[u][v] = savedEdgeValue
            G[v][u] = savedEdgeValue
            return False
        for i, e in enumerate(G[elem]):
            if e == 1 and not visited[i]:
                visited[i] = True
                q.append(i)
    # если v так и не встретилась, то ВОЗВРАЩАЕМ в граф ребро e и выдаем положительный результат
    G[u][v] = savedEdgeValue
    G[v][u] = savedEdgeValue
    return True



# считываем первую строку
N, u, v = map(int, input().split())

edges = []
# считываем ребра
while True:
    try:
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    except EOFError:
        break
# создаем представление графа для обхода
G = edges2matrix(N, edges)
# делаем работу и печатаем результат
print(is_safe(G, (u, v)))