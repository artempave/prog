def binSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem > max(A) or elem < min(A) or A == []:
        return None
    # определим верхнюю границу и вызовем рекурсивную функцию
    hi = len(A) - 1
    return binSearchRec(A, elem, 0, hi)


def binSearchRec(A, elem, lo, hi):
    # если подмассив пустой, то делать нечего
    if A[lo:hi + 1] == []:
        return -1
    # определяем средний элемент
    mid = (lo + hi) // 2
    # выполняем сравнение и рекурсивный вызов на одной из половин
    print(A[mid], end=" ")
    if A[mid] == elem:
        return mid
    elif A[mid] > elem:
        return binSearchRec(A, elem, lo, mid - 1)
    else:
        return binSearchRec(A, elem, mid + 1, hi)


if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))
    chec = binSearch(A, elem)
    if chec == None:
        print(chec)
