def print_help(A, rang_1, rang_2):
    s1 = ""
    if rang_1[0] > 0:
        s1 += " ".join(map(str, A[:rang_1[0]])) + " "
    if rang_1[1] >= rang_1[0]:
        s1 += "[" + " ".join(map(str, A[rang_1[0]:rang_1[1] + 1])) + "] "
    else:
        s1 += "[] "
    if rang_1[1] < rang_2[0]:
        s1 += " ".join(map(str, A[rang_1[1] + 1:rang_2[0]]))
    if rang_2[1] >= rang_1[0]:
        s1 += " [" + " ".join(map(str, A[rang_2[0]:rang_2[1] + 1])) + "]"
    else:
        s1 += " []"
    if rang_2[1] < len(A) - 1:
        s1 += " " + " ".join(map(str, A[rang_2[1] + 1:]))
    print(s1)


def partition(A, left, right):
    i = left + 1
    j = right
    if len(A[left:right + 1]) <= 1:
        return left
    while i <= j:
        while A[i] < A[left] and i < right:
            i += 1
        while A[j] > A[left] and j > left:
            j -= 1
        if i > j:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        if j != right:
            j -= 1
    A[left], A[j] = A[j], A[left]
    return j


def quickSortRec(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1
    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right or len(A) == 1 or A == []:
        return
    # производим разбиение с помощью partition
    p = partition(A, left, right)
    if verbose:
        print_help(A, (left, p - 1), (p + 1, right))
    else:
        print(" ".join(map(str, A)))
    # рекурсивно сортируем обе части
    quickSortRec(A, left, p - 1, verbose)
    quickSortRec(A, p + 1, right, verbose)


A = list(map(int, input().split()))
try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False

quickSortRec(A, 0, None, verbose)
