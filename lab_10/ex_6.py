# данный класс можно скопировать из упражнения 10.5, только при этом не забудьте
# изменить названия полей и методов на требуемые и не забудьте про аннотирование типов!
# не забудьте про аннотирование типов!
from typing import List


class UnionFind:
    # конструктор, создающий пустой массив для хранения СНМ
    def __init__(self) -> None:
        self._id: List[int] = []
        self._rank: List[int] = []

    def make_set(self, x: int) -> None:
        self._id.append(x)
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


# Этот код менять не нужно. При корректной реализации класса UnionFind он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

uf = UnionFind()
for i in range(10):
    uf.make_set(i)
print(uf.connected(6, 2))
print(uf.connected(9, 7))
uf.union_set(9, 0)
uf.union_set(8, 3)
uf.union_set(1, 4)
print(uf.connected(7, 6))
uf.union_set(6, 9)
uf.union_set(7, 4)
uf.union_set(1, 6)
uf.union_set(0, 6)
print(uf.connected(9, 5))
uf.union_set(1, 8)
uf.union_set(7, 9)
print(uf.connected(9, 8))
print(uf.connected(1, 2))
uf.union_set(1, 6)
print(uf)
