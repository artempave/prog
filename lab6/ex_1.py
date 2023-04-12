def merge(A, left, mid, right):
    # вспомогательный массив, в который будут сливаться элементы
    AUX = []
    # список, в который мы будем записывать порядок сливания элементов
    indexes = []
    # Инициализируем указатели i и j
    i = left
    j = mid + 1
    # Цикл, осуществляющий слияние
    while (i <= mid and j <= right):
        if A[i] <= A[j]:
            indexes.append(i)
            AUX.append(A[i])
            i += 1
        else:
            indexes.append(j)
            AUX.append(A[j])
            j += 1
    # Дописываем хвост (почитайте справку к функции extend для списков) и не забываем про indexes
    if i == mid + 1:
        AUX.extend(A[j:right + 1])
        indexes.extend([i for i in range(j, right+1)])
    else:
        AUX.extend(A[i:mid + 1])
        indexes.extend([i for i in range(i, mid+1)])
    # Возвращаем назад в массив A результат нашей работы (обратите внимание на присваивание срезу!)
    A[left:right + 1] = AUX
    return indexes



mas_1 = list(map(int, input().split()))
mas_2 = list(map(int, input().split()))
right = len(mas_1) + len(mas_2) - 1
mid = len(mas_1) - 1
mas_1.extend(mas_2)
indexes = merge(mas_1, 0, mid, right)
print(" ".join(map(str, mas_1)))
print(" ".join(map(str, indexes)))