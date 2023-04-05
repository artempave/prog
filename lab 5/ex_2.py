from functools import reduce

def HammingDistance(s1, s2):
    return reduce(lambda x, y: x + (1 if y[0] != y[1] else 0), zip(s1, s2), 0)

def Neighbours(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {"C", "G", "A", "T"}
    Neighborhood = set()
    # Рекурсивно находим d-соседей суффикса Pattern
    SuffixNeighbors = Neighbours(Pattern[1:], d)
    # Цикл по всем найденным соседям - шаг 2 алгоритма (рекурсивная часть)
    for i in SuffixNeighbors:
        if HammingDistance(i, Pattern[1:]) < d:
            for x in {'A', 'C', 'G', 'T'}:
                Neighborhood.add(x + i)
        else:
            Neighborhood.add(Pattern[0] + i)
    # Не будем преобразовывать ответ в список и сортировать его
    # Помните - то, что мы здесь возвращаем, мы же потом и используем на верхних шагах рекурсии!
    return Neighborhood

arr = input()
n = int(input())
ans = list(Neighbours(arr, n))
ans.sort()
print("\n".join(ans))
