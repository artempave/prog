from typing import List


class QuickFind:
    _id: List[int]

    def __init__(self) -> None:
        self._id = []

    def make_set(self) -> None:
        self._id.append(len(self._id))

    def find_set(self, x: int) -> int:
        return self._id[x]

    def __str__(self) -> str:
        return " ".join(map(str, self._id))

    def union_set(self, x: int, y: int) -> None:
        x_id: int = self.find_set(x)
        y_id: int = self.find_set(y)
        l: int = len(self._id)
        for i in range(l):
            if self._id[i] == y_id:
                self._id[i] = x_id

    def connected(self, x: int, y: int) -> bool:
        return self.find_set(x) == self.find_set(y)


N: int = int(input())
uf: QuickFind = QuickFind()
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
            arr: list = line.split()
            op: str = arr[0]
            x: int = int(arr[1])
            y: int = int(arr[2])
            if op == "+":
                uf.union_set(x, y)
            elif op == "?":
                print(uf.connected(x, y))
    except EOFError:
        break
