from lab6.ex_4 import partition


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


if __name__ == '__main__':
    A = list(map(int, input().split()))
    try:
        verbose = input()
        if verbose == 'verbose':
            verbose = True
    except EOFError:
        verbose = False
    quickSortRec(A, 0, None, verbose)
