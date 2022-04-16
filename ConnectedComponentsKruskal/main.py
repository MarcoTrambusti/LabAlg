# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import networkx as nx
# generazione di grafi casuali con un numero di nodi a scelta ed una determinata probabilità di presenza di archi tra vertici
import numpy as np
from timeit import default_timer as timer
from RandomWeightedGraph import random_weighted_graph
from ConnectedComponents import Connect_comp
from Kruskal import MST_Kruskal

def printGraph(m):
    G = nx.from_numpy_matrix(m, parallel_edges=True, create_using=nx.DiGraph)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, arrows=True, arrowstyle="->", connectionstyle="arc3,rad=0.1")
    labels = nx.get_edge_attributes(G, "weight", )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.6, clip_on=False)
    plt.show()

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
    KruskalTime=[]
    ConnectedTime=[]
    m=0
    n=0
    for i in range(3,50):
        for j in range(200):
            wg=random_weighted_graph(10,i,0.35)
            tK=timer()
            MST_Kruskal(wg,i)
            tK=timer()-tK
            tc=timer()
            Connect_comp(wg,i)
            tc=timer()-tc
            m+=tK
            n+=tc
        m/=200
        n/=200
        KruskalTime.append(m)
        ConnectedTime.append(n)
    return KruskalTime,ConnectedTime

def advancedTest2():
    KruskalTime=[]
    ConnectedTime=[]
    m=0
    n=0
    for i in range(0,100):
        for j in range(200):
            wg=random_weighted_graph(10,30,i/100)
            tK=timer()
            MST_Kruskal(wg,30)
            tK=timer()-tK
            tc=timer()
            Connect_comp(wg,30)
            tc=timer()-tc
            m+=tK
            n+=tc
        m/=200
        n/=200
        KruskalTime.append(m)
        ConnectedTime.append(n)
    return KruskalTime,ConnectedTime

def plot(K,title):
    x = np.arange(0, 50, 10)
    y = np.arange(0)
    plt.plot(K)
    plt.title(title)
    plt.xlabel('nodes')
    plt.ylabel('time ')
   # plt.legend(['Kruskal', 'Connected components'])
    plt.show()

if __name__ == '__main__':
    n = 5
    p = 0.3
    w = 10

    kruskalTime=[]
    connectedTime=[]
    kruskalTimeProb = []
    connectedTimeProb = []

    SimpleTest()
    kruskalTime,connectedTime=advancedTest()
    kruskalTimeProb,connectedTimeProb=advancedTest2()

    plot(kruskalTime,"test incremento nodi Kruskal")
    plot(connectedTime, "test incremento nodi componenti connesse")
    plot(kruskalTimeProb,"test incremento probabilità Kruskal")
    plot(connectedTimeProb,"test incremento probabilità componenti connesse")

    """

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
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
