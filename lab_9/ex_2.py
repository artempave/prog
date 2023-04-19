# декомпозируем нашу задачу на ряд подзадач, каждую из которых будет выполнять отдельная функция

# данная функция принимает на вход количество вершин и список ребер, каждое из которых
# задано кортежом (структурой tuple)
def edges2matrix(N, edges):
    # создаем матрицу размером NxN из нулей
    matrix = [[0] * N for _ in range(N)]
    # пробегаемся по ребрам, записываем информацию в матрицу
    for edge in edges:
        matrix[edge[0]][edge[1]] = 1
    return matrix


# функция возвращает True, если граф неориентированный, и False иначе
def isUndirected(matrix):
    # размеры матрицы мы можем определить из нее самой
    N = len(matrix)
    # пробегаемся с помощью двойного цикла и возвращаем False, если найдем хотя бы одну асимметрию
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != matrix[j][i]:
                return False
    # если асимметрий не было найдено, значит граф - неориентированный
    return True


# функция принимает на вход строку и возвращает список ребер, где каждое ребро задано кортежом
def makeEdges(s):
    # превращаем строку в список лексем с помощью split
    lst = s.split()
    # создаем пустой список ребер
    edges = []
    # бежим по лексемам с шагом 2 и создаем ребра
    l = len(lst)
    for i in range(0, len(lst), 2):
        edges.append((int(lst[i]), int(lst[i + 1])))
    return edges


# печатаем матрицу
def print_matrix(matrix):
    for n in matrix:
        print(" ".join(map(str, n)))


# считываем количество вершин
N = int(input())
# считываем и формируем список ребер
edges = makeEdges(input())
# переводим список ребер в матрицу смежности
matrix = edges2matrix(N, edges)
# печатаем тип графа и матрицу смежности
if isUndirected(matrix):
    print("undirected")
else:
    print("directed")
print_matrix(matrix)