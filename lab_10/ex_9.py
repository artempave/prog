# не забудьте про аннотирование типов!
from typing import List


class Heap:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.heap: List[int] = []

    def left_son(self, p: int) -> int:
        return 2 * p + 1

    def right_son(self, p: int) -> int:
        return 2 * p + 2

    def parent(self, p: int) -> int:
        if p == 0:
            return 0
        return (p - 1) // 2

    def min_son(self, p: int) -> int:
        l: int = self.left_son(p)
        r: int = self.right_son(p)
        _len = len(self.heap)
        if l >= _len:
            return -1
        elif r >= _len or self.heap[l] <= self.heap[r]:
            return l
        return r

    def sift_up(self, p: int) -> None:
        if p == 0:
            return
        elem: int = self.heap[p]
        while p > 0:
            prnt: int = self.parent(p)
            if self.heap[prnt] < elem:
                break
            self.heap[p] = self.heap[prnt]
            p = prnt
        self.heap[p] = elem

    def sift_down(self, p: int) -> None:
        minCh: int = self.min_son(p)
        l: int = len(self.heap)
        while minCh != -1 and self.heap[p] > self.heap[minCh]:
            self.heap[p], self.heap[minCh] = self.heap[minCh], self.heap[p]
            p = minCh
            minCh = self.min_son(p)

    # метод для добавления элемента x в кучу
    def add(self, x: int) -> None:
        self.heap.append(x)
        self.sift_up(len(self.heap) - 1)

    # метод для возврата минимума
    def min(self) -> int:
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    # метод для возврата минимума и удаления его из кучи
    def get_min(self) -> int:
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        _min: int = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return _min

    # печать массива с бинарным деревом кучи
    def __str__(self) -> str:
        return " ".join(map(str, self.heap))


# Этот код менять не нужно. При корректной реализации класса Heap он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
heap = Heap()
heap.add(1)
heap.add(10)
heap.add(8)
heap.add(32)
heap.add(11)
heap.add(38)
heap.add(42)
heap.add(78)
heap.add(31)
print(heap)