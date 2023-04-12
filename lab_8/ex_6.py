class Graph:
    def __init__(self, V=None, E=None):
        self.V = []
        self.flag_V = []
        self.E = []
        self.flag_E = []
        if V != None:
            for v in V:
                self.add_vertex(v)
        if E != None:
            for e in E:
                self.add_edge(e)

    def __str__(self):
        s1 = "vertices:\n" + " ".join(map(str, self.vertices())) + "\n"
        s2 = "edges:\n" + "\n".join(map(lambda x: str(x[0]) + " -> " + str(x[1]), self.edges()))
        return s1 + s2

    def __setitem__(self, x, d):
        if (type(x) == tuple):
            i = self.E.index(x)
            self.flag_E[i] = d
        else:
            i = self.V.index(x)
            self.flag_V[i] = d

    def __getitem__(self, x):
        if (type(x) == tuple):
            i = self.E.index(x)
            return self.flag_E[i]
        else:
            i = self.V.index(x)
            return self.flag_V[i]

    def add_vertex(self, v):
        if v not in self.V:
            self.V.append(v)
            self.flag_V.append(None)

    def add_edge(self, e):
        if e not in self.E:
            self.E.append(e)
            self.flag_E.append(1)
        else:
            self.flag_E[self.E.index(e)] += 1

    def edges(self):
        for e in self.E:
            yield e

    def vertices(self):
        self.V.sort()
        for v in self.V:
            yield v

    def outgoing(self, v):
        for help_e in self.E:
            if v == help_e[0]:
                yield help_e


def walk(G, path=[]):
    V = list(G.vertices())
    if V == []:
        return path
    if path == []:
        path.append(V[0])
    v = path[-1]
    for e in G.outgoing(v):
        if G[e] > 0:
            G[e] = G[e] - 1
            path.append(e[1])
            return walk(G, path)
    return path


def rewind(G, path):
    if path == [] or path[0] != path[-1]:
        return path
    flag = False
    for v in path:
        for p in G.outgoing(v):
            if G[p] != 0:
                i = v
                flag = True
                break
        if flag:
            break
    if flag:
        k = path.index(i)
        return path[k:] + path[1:k + 1]
    else:
        return path


def eulerian_cycle(G):
    # конструируем первоначальный цикл из первой в лексикографическом порядке вершины графа
    cycle = list(walk(G))
    # если цикл пустой или цикл - не цикл, то заканчиваем работу
    if cycle == [] or cycle[0] != cycle[-1]:
        return None
    # делаем перемотку, продолжаем идти, делаем перемотку, продолжаем идти и т.д.
    # как только цикл перестанет меняться (расти), заканчиваем работу и возвращаем результат
    while True:
        k = list(cycle)
        cycle = list(rewind(G, cycle))
        if cycle == k:
            return cycle
        cycle = list(walk(G, cycle))
        if cycle[0] != cycle[-1]:
            return None
    return cycle


# функция для проверки, остались ли в графе непосещенные ребра
def check_cycle(G):
    # перебираем все ребра и смотрим, есть ли непосещенные
    for e in G.edges():
        if G[e] != 0:
            return False
    # если все ребра перебрали и непосещенных не нашли, возвращаем положительный ответ
    return True


# считываем вершины
vertices = list(map(int, input().split()))
# конструируем граф
G = Graph(vertices, [])
# считываем ребра и добавляем их в граф
while True:
    try:
        e = tuple(map(int, input().split()))
    except EOFError:
        break
    G.add_edge(e)

# находим цикл, проверяем, все ли корректно и печатаем результат
cycle = eulerian_cycle(G)
if check_cycle(G):
    if cycle != None:
        print(" ".join(map(str, cycle)))
    else:
        print(None)
else:
    print(None)