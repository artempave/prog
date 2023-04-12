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

    def get_list_V(self):
        return self.V

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


def rewind(G, path):
    # если пусть пустой или не является циклом, завершаем работу
    if path == [] or path[0] != path[-1]:
        return path
    # перебираем вершины пути и ищем первую с ненулевыми исходящими ребрами
    flag = False
    for v in path:
        for p in G.outgoing(v):
            if G[p] != 0:
                i = v
                flag = True
                break
        if flag:
            break
    # если на предыдущем шаге нашли подходящую вершину, конструируем новый путь,
    # иначе возвращаем старый
    if flag:
        k = path.index(i)
        return path[k:] + path[1:k + 1]
    else:
        return path


# Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

g = Graph([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])
g[(1, 2)] = 0
g[(3, 4)] = 0
g[(4, 1)] = 0
g[(2, 3)] = 1
print(rewind(g, [1, 2, 3, 4, 1]))
print(rewind(g, [2, 3, 4, 1, 2]))
