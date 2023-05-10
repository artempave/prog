# для метода sift_down понадобятся вспомогательные методы left_son, right_son, min_son
# не забудьте про аннотирование типов!
from typing import List

def left_son(p: int) -> int:
    # возвращаем индекс левого сына элемента p
    return 2 * p + 1

def right_son(p: int) -> int:
    # возвращаем индекс правого сына элемента p
    return 2 * p + 2

def min_son(p: int) -> int:
    # возвращаем индекс минимального сына элемента p или -1, если p - лист
    l: int = left_son(p)
    r: int = right_son(p)
    _len = len(heap)
    if l >= _len:
        return -1
    elif r >= _len or heap[l] <= heap[r]:
        return l
    return r

def sift_down(heap: List[int], p: int) -> None:
    minCh: int = min_son(p)
    l: int = len(heap)
    # пока мы не в листе и текущий элемент больше минимального из сыновей,
    # меняем их местами и погружаемся ниже
    while minCh != -1 and heap[p] > heap[minCh]:
        heap[p], heap[minCh] = heap[minCh], heap[p]
        p = minCh
        minCh = min_son(p)

# считать массив heap
heap: List[int] = list(map(int, input().split()))

# считать индекс всплываемого элемента
p: int = int(input())

# осуществляем всплытие
sift_down(heap, p)

# напечатать heap
print(" ".join(map(str, heap)))