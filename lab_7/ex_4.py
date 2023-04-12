def insert2Mas(A, n, i, elem):
    # если вставлять уже некуда, пишем full
    if len(A) == n:
        print("full")
        return
    # в цикле печатаем переносы элементов
    for j in reversed(range(i + 1, n + 1)):
        print('A[{}] = A[{}]'.format(j, j - 1))
        A[j] = A[j - 1]
    # печатаем копирование элемента elem в нужное место
    print('A[{}] = {}'.format(i, elem))

if __name__ == '__main__':
    porametrs = list(map(int, input().split()))
    A = list(map(int, input().split()))
    insert2Mas(A, porametrs[0], porametrs[1], porametrs[2])