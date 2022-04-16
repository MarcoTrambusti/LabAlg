from ConnectedComponents import UnionFind,Connect_comp

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

    while len(A) <n-1:
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