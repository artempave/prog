# возможно какие-то методы можно скопировать из упражнения 10.1
# не забудьте про аннотирование типов!
from typing import List


class UnionFind:
    # конструктор, создающий пустой массив для хранения СНМ
    def __init__(self) -> None:
        self._id: List[int] = []

    def make_set(self) -> None:
        self._id.append(len(self._id))

    def root(self, x: int) -> int:
        while x != self._id[x]:
            x = self._id[x]
        return x

    def __str__(self) -> str:
        return " ".join(map(str, self._id))

    def union_set(self, x: int, y: int) -> None:
        root_x: int = self.root(x)
        root_y: int = self.root(y)
        self._id[root_y] = root_x

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
