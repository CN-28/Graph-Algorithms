from dimacs import *
from os import listdir
from os.path import join

class MakeSet:
    def __init__(self, val=None):
        self.val = val
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent    


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1


def findUnionSolve(V, L, s, t):
    L.sort(key = lambda x : x[2], reverse = True)
    forest = [MakeSet(i) for i in range(V + 1)]

    for u, v, c in L:
        union(forest[u], forest[v])
        if find(forest[s]) == find(forest[t]):
            return c
        

mypath = "lab1\graphs"
for file in listdir(mypath):
    V, L = loadWeightedGraph(join(mypath, file))
    print(file, findUnionSolve(V, L, 1, 2))