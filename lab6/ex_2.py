def print_good(A, left, mid, right):
    s = ""
    if left != 0:
        s += " ".join(map(str, A[:left])) + " "
    s += "[" + " ".join(map(str, A[left:mid + 1])) + "] "
    s += "[" + " ".join(map(str, A[mid + 1: right + 1])) + "]"
    if right != len(A) - 1:
        s += " " + " ".join(map(str, A[right + 1:]))
    print(s)


def merge(A, left, mid, right):
    AUX = []
    i = left
    j = mid + 1
    while (i <= mid and j <= right):
        if A[i] <= A[j]:
            AUX.append(A[i])
            i += 1
        else:
            AUX.append(A[j])
            j += 1
    if i == mid + 1:
        AUX.extend(A[j:right + 1])
    else:
        AUX.extend(A[i:mid + 1])
    A[left:right + 1] = AUX.copy()


def mergeSort(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1
    if len(A[left:right + 1]) <= 1:
        return
    # определяем середину
    mid = (left + right) // 2
    # рекурсивно сортируем обе половины
    mergeSort(A, left, mid, verbose)
    mergeSort(A, mid + 1, right, verbose)
    if verbose:
        print_good(A, left, mid, right)
    else:
        print(" ".join(map(str, A)))
    merge(A, left, mid, right)
    # печатаем массив и производим слияние с помощью функции merge

if __name__ == '__main__':
    A = list(map(int, input().split()))
    try:
        verbose = input()
        if verbose == 'verbose':
            verbose = True
    except EOFError:
        verbose = False
    mergeSort(A, 0, len(A) - 1, verbose)
    print(" ".join(map(str, A)))