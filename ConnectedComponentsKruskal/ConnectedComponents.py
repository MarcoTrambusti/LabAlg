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
