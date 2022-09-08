from ConnectedComponents import UnionFind,Connect_comp

def MST_Kruskal(m, n):
    A=[]
    u = UnionFind()
    mincost = 0
    if len(Connect_comp(m, n).set) > 1:
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
        mincost += min

    return A,mincost