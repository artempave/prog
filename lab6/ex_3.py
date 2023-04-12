from lab6.ex_1 import merge


def mergeSortNonRec(A):
    # запоминаем длину массива
    n = len(A)
    width = 1
    while width < n:
        i = 0
        while i < n:
            merge(A, i, min(i + width - 1, n - 1), min(i + 2 * width - 1, n - 1))
            i += 2 * width
        # не забываем увеличивать width на нужное значение
        width *= 2
        print(" ".join(map(str, A)))

if __name__ == '__main__':
    A = list(map(int, input().split()))
    mergeSortNonRec(A)