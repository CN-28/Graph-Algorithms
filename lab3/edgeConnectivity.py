import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join


class Node:
    def __init__(self):
        self.edges = {}
    
    def addEdge(self, v, weight):
        self.edges[v] = self.edges.get(v, 0) + weight

    def delEdge(self, v):
        del self.edges[v]
    

def mergeVertices(G, u, v):
    if v in G[u].edges:
        G[u].delEdge(v)
        G[v].delEdge(u)

    for s in G[v].edges:
        print(s)
        edge = G[v].edges[s]
        G[v].delEdge(s)
        G[s].delEdge(v)
        
        G[u].edges[s] = edge + G[u].edges.get(s, 0)
        G[s].edges[u] = G[u].edges[s]
        


if __name__ == "__main__":
    mypath = "lab3\\graphs-lab3"
    """
    for file in listdir(mypath):
        V, L = loadWeightedGraph(join(mypath, file))
        G = [Node() for _ in range(V + 1)]
        for u, v, c in L:
            G[u].addEdge(v, c)
            G[v].addEdge(u, c)
    """
    G = [Node() for _ in range(3)]
    G[0].addEdge(1, 2)
    G[1].addEdge(0, 2)
    G[1].addEdge(2, 3)
    G[2].addEdge(1, 3)
    for u in G:
        print(u.edges)
    mergeVertices(G, 0, 1)
    for u in G:
        print(u.edges)