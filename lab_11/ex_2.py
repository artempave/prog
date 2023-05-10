# функция для представления графа в виде, удобном для обхода виде
from typing import List, Tuple

def my_sort(arr) -> None:
    l:int = len(arr)
    flag: int = 0
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j][1] > arr[j+1][1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                flag = 1
        if flag == 0:
            break
        else:
            flag = 0

def is_safe(G: List[List[int]], e: Tuple[int, int]) -> bool:
    u, v = e
    savedEdgeValue: int = G[u][v]
    G[u][v] = 0
    G[v][u] = 0
    visited: List[bool] = [False] * len(G)
    q: List[int] = [u]
    visited[u] = True
    while q:
        elem: int = q.pop(0)
        if elem == v:
            G[u][v] = savedEdgeValue
            G[v][u] = savedEdgeValue
            return False
        for i, e in enumerate(G[elem]):
            if e != 0 and not visited[i]:
                visited[i] = True
                q.append(i)
    G[u][v] = savedEdgeValue
    G[v][u] = savedEdgeValue
    return True

# Мы будем параллельно использовать сразу два представления графа - список ребер для Крускала
# и матрицу смежности (или ваше на выбор) для работы функции is_safe
def Kruskal_MST(N: int, edges) -> List[Tuple[int, int]]:
    # инициализируем матрицу смежности графом с N вершинами и БЕЗ ребер
    G: List[List[int]] = [[0]*N for _ in range(N)]
    # создаем пустой список для хранения ребер остова
    A: List[Tuple[int, int]] = []
    # сортируем список ребер
    my_sort(edges)
    # перебираем ребра и выполняем алгоритм
    s: int = 0
    for edge in edges:
        if is_safe(G, edge[0]):
            s += edge[1]
            u, v = edge[0]
            G[u][v] = 1
            G[v][u] = 1
            A.append(edge[0])
    # возвращаем остов, а представление G в виде матрицы смежности на больше не нужно
    A.sort()
    print(s)
    return A

# функция печати остова в нужном формате
def print_spanning_tree(A: List[Tuple[int, int]]):
    for edge in A:
        print(f"({edge[0]}, {edge[1]})", end = " ")



# считываем первую строку
N: int = int(input())

edges: List[int]= []
# считываем ребра
while True:
    try:
        edge = list(map(int, input().split()))
        edges.append([(edge[0], edge[1]), edge[2]])
    except EOFError:
        break
# делаем работу и печатаем результат
A: List[Tuple[int, int]] = Kruskal_MST(N, edges)
print_spanning_tree(A)