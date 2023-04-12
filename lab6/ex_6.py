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


def quickSort3Way(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1
    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return
    # инициализируем всевозможные указатели
    v = A[left]
    i = left + 1
    lt = left
    gt = right
    # производим трехпутевое разбиение за один проход в соответствии с алгоритмом
    while i <= gt:
        if A[i] < v:
            A[i], A[lt] = A[lt], A[i]
            i += 1
            lt += 1
        elif A[i] > v:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    # печатаем массив в нужном формате
    if verbose:
        print_help(A, (left, lt - 1), (gt + 1, right))
    else:
        print(" ".join(map(str, A)))
        # print("(",left, lt - 1, ")", "(", gt + 1, right, ")")
    # рекурсивно сортируем обе части (кроме той, что равна опорному элементу!)
    quickSort3Way(A, left, lt - 1, verbose)
    quickSort3Way(A, gt + 1, right, verbose)


A = list(map(int, input().split()))
try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False

quickSort3Way(A, 0, None, verbose)

