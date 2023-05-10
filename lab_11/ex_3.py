from typing import List, Tuple


class UnionFind:
    def __init__(self) -> None:
        self._id: List[int] = []
        self._rank: List[int] = []

    def make_set(self) -> None:
        self._id.append(len(self._id))
        self._rank.append(0)

    def root(self, x: int) -> int:
        our_root: List[int] = []
        while x != self._id[x]:
            our_root.append(x)
            x = self._id[x]
        element: int
        for element in our_root:
            self._id[element] = x
        return x

    def __str__(self) -> str:
        return " ".join(map(str, self._id)) + "\n" + " ".join(map(str, self._rank))

    def union_set(self, x: int, y: int) -> None:
        root_x: int = self.root(x)
        root_y: int = self.root(y)
        if root_x == root_y:
            return
        if self._rank[root_x] < self._rank[root_y]:
            self._id[root_x] = root_y
        elif self._rank[root_x] > self._rank[root_y]:
            self._id[root_y] = root_x
        else:
            self._id[root_y] = root_x
            self._rank[root_x] = self._rank[root_y] + 1

    def connected(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


def Kruskal_MST_optimal(N: int, edges: List[Tuple[int, int, int]]) -> Tuple[List[Tuple[int, int, int]], UnionFind]:
    # создаем СНМ со всеми вершинами
    uf: UnionFind = UnionFind()
    for i in range(N):
        uf.make_set()
    # создаем пустой список для хранения ребер остова
    A: List[Tuple[int, int, int]] = []
    u: int
    v: int
    l: int
    s: int = 0
    # сортируем список ребер
    edges.sort(key=lambda x: x[2])
    # перебираем ребра и выполняем алгоритм
    for edge in edges:
        u, v, l = edge
        if not uf.connected(u, v):
            s += l
            uf.union_set(u, v)
            A.append(edge)
    # возвращаем остов и СНМ (для дальнейшей печати)
    A.sort()
    print(s)
    return A, uf


# функция печати остова в нужном формате
def print_spanning_tree(A: List[Tuple[int, int, int]]) -> None:
    l = len(A)
    for i in range(l):
        if i == l - 1:
            print(f"({A[i][0]}, {A[i][1]})")
        else:
            print(f"({A[i][0]}, {A[i][1]})", end=" ")


# считываем количество вершин
N = int(input())

edges = []
# считываем ребра
while True:
    try:
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    except:
        break

# делаем работу и печатаем результат
A, uf = Kruskal_MST_optimal(N, edges)
print_spanning_tree(A)
print(uf)