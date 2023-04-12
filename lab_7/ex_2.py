def interpolSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem < A[0] or elem > A[-1]:
        print(None)
        return None
    # определим верхнюю границу и вызовем рекурсивную функцию
    return interpolSearchRec(A, elem, 0, len(A) - 1)


def interpolSearchRec(A, elem, lo, hi):
    # если подмассив пустой ИЛИ elem за границами диапазона, то делать нечего
    if A[lo:hi + 1] == [] or (elem < A[lo] or elem > A[hi]):
        return -1
    # если левая и правая границы совпадают, то mid по формуле вычислять нельзя! (почему?)
    if A[lo] == A[hi]:
        mid = lo
    else:
        mid = lo + round((elem - A[lo]) * (hi - lo) / (A[hi] - A[lo]))
    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        print(A[mid])
        return mid
    elif A[mid] > elem:
        print(A[mid], end=" ")
        return interpolSearchRec(A, elem, lo, mid - 1)
    else:
        print(A[mid], end=" ")
        return interpolSearchRec(A, elem, mid + 1, hi)

if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))
    chec = interpolSearch(A, elem)