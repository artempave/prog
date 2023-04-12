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
        self.E.sort()
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
    # если граф пустой, то делать ничего не нужно, завершаем рекурсию
    V = list(G.vertices())
    if V == []:
        return path
    # если путь пустой, то добавляем в него первую в лексикографическом порядке вершину графа
    if path == []:
        path.append(V[0])
    # С помощью outgoing() пытаемся найти ребро из последней в пути path вершины.
    # Если нашли, модифицируем метку, добавляем новую вершину в path и делаем рекурсивный вызов.
    # Не забудьте, что функция walk должна вернуть путь!
    v = path[-1]
    for e in G.outgoing(v):
        if G[e] > 0:
            G[e] = G[e] - 1
            path.append(e[1])
            return walk(G, path)
    # если свободных ребер нет, то просто возвращаем path
    return path


# Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

g = Graph([1, 2, 3], [(1, 2), (2, 3), (3, 1)])
g[(1, 2)] = 1
g[(2, 3)] = 1
g[(3, 1)] = 0
print(walk(g, [1]))
print(g[(1, 2)])
print(g[(2, 3)])
