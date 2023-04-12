class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
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

    # метод конструирования строкового представления графа
    def __str__(self):
        s1 = "vertices:\n" + " ".join(map(str, self.vertices())) + "\n"
        s2 = "edges:\n" + "\n".join(map(lambda x: str(x[0]) + " -> " + str(x[1]), self.edges()))
        return s1 + s2

    # метод добавления метки вершине или ребру
    def __setitem__(self, x, d):
        if (type(x) == tuple):
            i = self.E.index(x)
            self.flag_E[i] = d
        else:
            i = self.V.index(x)
            self.flag_V[i] = d

    # метод возврата метки вершины или ребра
    def __getitem__(self, x):
        if (type(x) == tuple):
            i = self.E.index(x)
            return self.flag_E[i]
        else:
            i = self.V.index(x)
            return self.flag_V[i]

    # Добавляет в граф вершину v. Метка вершины должна быть None.
    def add_vertex(self, v):
        if v not in self.V:
            self.V.append(v)
            self.flag_V.append(None)

    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    def add_edge(self, e):
        if e not in self.E:
            self.E.append(e)
            self.flag_E.append(None)

    # генератор или итератор, перечисляющий все рёбра графа
    def edges(self):
        for e in self.E:
            yield e

    # генератор или итератор, перечисляющий все вершины графа
    def vertices(self):
        for v in self.V:
            yield v

    # генератор или итератор, перечисляющий все рёбра, выходящие из вершины v
    def outgoing(self, v):
        for help_e in self.E:
            if v == help_e[0]:
                yield help_e


# Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

g = Graph()
g.add_vertex("u")
g.add_vertex("v")
g.add_vertex("w")
g.add_edge(("u", "v"))
g.add_edge(("u", "w"))
g.add_edge(("v", "w"))
print(g)
print(list(g.vertices()))
print(list(g.edges()))
print(list(g.outgoing("u")))
print(list(g.outgoing("w")))
g["u"] = 1
g[("u", "v")] = 42
print(g["v"])
print(g["u"])
print(g[("u", "v")])
print(g[("v", "w")])
g2 = Graph(["a", "b"], [("a", "b"), ("b", "a")])
print(g2)
