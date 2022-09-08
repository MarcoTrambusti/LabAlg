# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
from RandomWeightedGraph import random_weighted_graph
from ConnectedComponents import Connect_comp
from Kruskal import MST_Kruskal

def advancedTest():
    KruskalTime=[]
    ConnectedTime=[]
    m=0
    n=0
    for i in range(3,200,5):
        for j in range(10):
            wg=random_weighted_graph(10,i,0.35)
            tK=timer()
            MST_Kruskal(wg,i)
            tK=timer()-tK
            tc=timer()
            Connect_comp(wg,i)
            tc=timer()-tc
            m+=tK
            n+=tc
        m/=10
        n/=10
        KruskalTime.append(m)
        ConnectedTime.append(n)
    return KruskalTime,ConnectedTime

def advancedTest2():
    KruskalTime=[]
    ConnectedTime=[]
    m=0
    n=0
    for i in range(0,100,2):
        for j in range(40):
            wg=random_weighted_graph(10,50,i/100)
            tK=timer()
            MST_Kruskal(wg,50)
            tK=timer()-tK
            tc=timer()
            Connect_comp(wg,50)
            tc=timer()-tc
            m+=tK
            n+=tc
        m/=40
        n/=40
        KruskalTime.append(m)
        ConnectedTime.append(n)
    return KruskalTime,ConnectedTime

def plot(K,title,l,i,txtX):
    x = np.arange(0,l,i)
    y = np.arange(0)
    plt.plot(x,K)
    plt.title(title)
    plt.xlabel(txtX)
    plt.ylabel('time ')
    plt.show()

if __name__ == '__main__':
    kruskalTime=[]
    connectedTime=[]
    kruskalTimeProb = []
    connectedTimeProb = []

    kruskalTime, connectedTime=advancedTest()
    kruskalTimeProb, connectedTimeProb=advancedTest2()

    plot(kruskalTime,"test incremento nodi Kruskal",200,5,"nodi")
    plot(connectedTime, "test incremento nodi componenti connesse",200,5,"nodi")
    plot(kruskalTimeProb,"test incremento probabilità Kruskal",100,2,"prob. presenza archi")
    plot(connectedTimeProb,"test incremento probabilità componenti connesse",100,2,"prob. presenza archi")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
