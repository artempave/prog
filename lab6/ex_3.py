def merge(A, left, mid, right):
    AUX = []
    indexes = []
    i = left
    j = mid + 1
    while (i <= mid and j <= right):
        if A[i] <= A[j]:
            indexes.append(i)
            AUX.append(A[i])
            i += 1
        else:
            indexes.append(j)
            AUX.append(A[j])
            j += 1
    if i == mid + 1:
        AUX.extend(A[j:right + 1])
        indexes.extend([i for i in range(j, right + 1)])
    else:
        AUX.extend(A[i:mid + 1])
        indexes.extend([i for i in range(i, mid + 1)])
    A[left:right + 1] = AUX
    return indexes


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