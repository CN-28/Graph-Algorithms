import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)


def lexBFS(G, u):
    subsets = [set(), set()]
    V = {s for s in range(1, len(G))}
    
    for v in G[u].out:
        subsets[1].add(v)
    
    visit_order = []
    subsets[0] = V - subsets[1]
    while subsets:
        u = subsets[-1].pop()
        visit_order.append(u)

        new_subsets = []
        for X in subsets:
            Y = set()
            K = set()

            for v in X:
                if v in G[u].out:
                    Y.add(v)
                else:
                    K.add(v)
                
            if K:
                new_subsets.append(K)
            if Y:
                new_subsets.append(Y)
        
        subsets = new_subsets
    
    return visit_order


def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n-1):
        for j in range(i+1, n-1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True
        

if __name__ == "__main__":
    mypath = "lab4\\graphs-lab4\\chordal"
    for file in listdir(mypath):
        print(file)
        V, L = loadWeightedGraph(join(mypath, file))
        G = [None] + [Node(u) for u in range(1, V + 1)]

        for u, v, _ in L:
            G[u].connect_to(v)
            G[v].connect_to(u)
        
        x = lexBFS(G, 1)
        print(checkLexBFS(G, x))
        print()
