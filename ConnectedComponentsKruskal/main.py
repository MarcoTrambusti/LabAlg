# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import networkx as nx
# generazione di grafi casuali con un numero di nodi a scelta ed una determinata probabilità di presenza di archi tra vertici
import numpy as np
from timeit import default_timer as timer



def adjacency_matrix(n, p):
    adjacency_matrix = np.random.binomial(1, p, (n, n))  # binomial(n,p,dimensione) mettendo n=1 ho una distribuzione di bernoulli ovvero 1*p
    return adjacency_matrix


# generazione di grafi pesati casuali
def random_weighted_graph(w, n, p):
    a = adjacency_matrix(n, p)
    weight = np.random.randint(1, w, (n, n))
    a *= weight
    return a


def printGraph(m):
    G = nx.from_numpy_matrix(m, parallel_edges=True, create_using=nx.DiGraph)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, arrows=True, arrowstyle="->", connectionstyle="arc3,rad=0.1")
    labels = nx.get_edge_attributes(G, "weight", )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.6, clip_on=False)
    plt.show()


#Struttura dati UNION-FIND
class DisjSet:
    def __init__(self, x):
        self.set = []
        for i in x:
            self.set.append(i)

        self.rp = self.set[0]

    def add(self, y):
        self.set.append(y)

    def union(self, y):
        self.set.extend(y.set)

    def contains(self, x):
        if x in self.set:
            return True


class UnionFind:
    def __init__(self):
        self.set = []

    def MakeSet(self, x):
        self.set.append(DisjSet(x))

    def Find(self, x):
        for s in self.set:
            if s.contains(x):
                return s

    def Union(self, x, y):
        if self.Find(x) and self.Find(y) and (self.Find(x) != self.Find(y)):
            z = self.Find(x).set + self.Find(y).set
            self.MakeSet(z)
            self.set.remove(self.Find(x))
            self.set.remove(self.Find(y))

    def FindSet(self, z):
        if self.Find(z):
            return self.Find(z).rp

#Ricerca componenti connesse
def Connect_comp(m, n):
    u = UnionFind()
    for i in range(n):
        u.MakeSet([i])

    for i in range(n):
        for j in range(n):
            if m[i][j] != 0 and u.FindSet(i) != u.FindSet(j):
                u.Union(i, j)
    return u


""""
MST-Kruskal(G,w)
A ← ∅
for ogni vertice v ∈ G.V
Make-Set(v)
//ordina gli archi di G.E in senso non decrescente rispetto al peso w
for ogni arco (u, v) ∈ G.E //preso in ordine di peso non decrescente
if Find-Set(u) ≠Find-Set(v)
A ← A ∪ {(u, v)}
Union(u, v)
return A
"""


def MST_Kruskal(m, n):
    A=[]
    u = UnionFind()
    #k = 0
    mincost = 0
    if len(Connect_comp(m, n).set) > 1:
        #print("graph is not connected")
        return 0
    for i in range(n):
        u.MakeSet([i])

    while len(u.set) > 1:
        min = float("inf")

        for i in range(n):
            for j in range(n):
                if u.Find(i) != u.Find(j) and m[i][j] < min and m[i][j] > 0:
                    min = m[i][j]
                    a = i
                    b = j

        A.append([a,b])
        u.Union(a, b)
        #k += 1
        #print('Edge {}:({}, {}) cost:{}'.format(k, a, b, min))
        mincost += min
    #print(u.set[0].set)
    #print("Minimum cost= {}".format(mincost))
    return A,mincost

def SimpleTest():
    n = 5
    w = 10
    print("prob 0%")
    print(random_weighted_graph(w, n, 0))
    print("prob 100%")
    print(random_weighted_graph(w, n, 1))
    print("prob 70%")
    print(random_weighted_graph(w, n, 0.7))

def advancedTest():
    data=[]
    m=0
    for i in range(3,50):
        for j in range(200):
            wg=random_weighted_graph(10,i,np.random.random(1))
            t=timer()
            MST_Kruskal(wg,i)
            t=timer()-t
            m+=t
        m/=200
        data.append(m)
    return data
if __name__ == '__main__':
    n = 5
    p = 0.3
    w = 10
    data=[]
    SimpleTest()
    data=advancedTest()
    plt.plot(data)
    plt.show()
    weightedgraph = random_weighted_graph(w, n, p)
    print(weightedgraph)

    A,m= MST_Kruskal(weightedgraph, n)
    print(A,"costo minimo",m)
    printGraph(weightedgraph)
    print()
    u = Connect_comp(weightedgraph, n)

    for s in u.set:
        print(s.set, s.set[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
