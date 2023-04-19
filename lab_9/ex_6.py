s = []


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
            self.flag_V.append(1)

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


def Graph_Traversal_Rec_1(G, start):
    s.append(start)
    G[start] = 0
    for e in G.outgoing(start):
        if G[e[1]] == 1:
            Graph_Traversal_Rec_1(G, e[1])


def Graph_Traversal_Rec_2(G, start):
    G[start] = 0
    for e in G.outgoing(start):
        if G[e[1]] == 1:
            Graph_Traversal_Rec_2(G, e[1])
            print(e[1], end=" ")


parametrs = input().split()
start = int(parametrs[0])
N = int(parametrs[1])
G = Graph([i for i in range(N)])
for i in range(N):
    e = list(map(int, input().split()))
    l = len(e)
    for j in range(l):
        if e[j] == 1:
            G.add_edge((i, j))
Graph_Traversal_Rec_1(G, start)
print(" ".join(map(str, s)))
for i in range(N):
    G[i] = 1
Graph_Traversal_Rec_2(G, start)
print(start)