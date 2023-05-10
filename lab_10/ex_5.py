# большую часть методов можно скопировать из упражнения 10.2
# не забудьте про аннотирование типов!
from typing import List


class UnionFind:
    # конструктор, создающий пустой массив для хранения СНМ
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


N: int = int(input())
uf: UnionFind = UnionFind()
_: int
for _ in range(N):
    uf.make_set()
while True:
    # считайте команду, определите ее тип и выполните ее, вызвав соответствующий метод uf
    try:
        line: str = input()
        if line == "print":
            print(uf)
        else:
            arr: List[str] = line.split()
            op: str = arr[0]
            x: int = int(arr[1])
            y: int = int(arr[2])
            if op == "+":
                uf.union_set(x, y)
            elif op == "?":
                print(uf.connected(x, y))
    except EOFError:
        break
