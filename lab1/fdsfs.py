from dimacs import *
class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0


def find(x):
    while x != x.parent:
        x = x.parent
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x.rank < y.rank:
            x, y = y, x
        
        y.parent = x
        if x.rank == y.rank:
            x.rank += 1
    

def solve(V, L, s, t):
    L.sort(key = lambda x : x[2])
    print(L)

V, L = loadWeightedGraph("lab1/graphs/g1")
print(solve(V, L, 1, 2))