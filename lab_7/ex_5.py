def insertMas2Mas(A, n, i, B):
    # если вставлять уже некуда, пишем full
    if len(A) - n < len(B):
        print("full")
        return
    # в цикле печатаем переносы элементов
    for j in reversed(range(i + len(B), n + len(B))):
        print('A[{}] = A[{}]'.format(j, j - len(B)))
        A[j] = A[j - len(B)]

    # в цикле печатаем копирование элементов из B в нужные места
    for j in range(i, i + len(B)):
        print('A[{}] = {}'.format(j, B[j - i]))

if __name__ == '__main__':
    porametrs = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    insertMas2Mas(A, porametrs[0], porametrs[1], B)