# Stoer-Wagner algorithm

import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join
from queue import PriorityQueue


class Node:
    def __init__(self):
        self.edges = {}
        self.isActive = True
        self.mergedWith = []
    
    def addEdge(self, v, weight):
        self.edges[v] = self.edges.get(v, 0) + weight

    def delEdge(self, v):
        del self.edges[v]
    

def mergeVertices(G, u, v):
    G[v].isActive = False
    G[u].mergedWith.append(v)
    if v in G[u].edges:
        G[u].delEdge(v)
        G[v].delEdge(u)

    for s in G[v].edges:
        edge = G[v].edges[s]
        G[s].delEdge(v)
        
        G[u].edges[s] = edge + G[u].edges.get(s, 0)
        G[s].edges[u] = G[u].edges[s]
    
    G[v].edges = {}
        

def minimumCutPhase(G):
    Q = PriorityQueue()
    u = 1
    visited = [False for _ in range(len(G))]
    sums = [G[v].edges.get(u, 0) for v in range(len(G))]
    visited[u] = True
    prev_last = 0
    last = u

    for v, cost in G[u].edges.items():
        Q.put((-cost, v))
    
    while not Q.empty():
        c, u = Q.get()
        if visited[u]:
            continue

        visited[u] = True
        cut = -c
        prev_last, last = last, u
        for v in G[u].edges:
            sums[v] += G[v].edges.get(u, 0)
            if sums[v] > 0:
                Q.put((-sums[v], v))
        
    return last, prev_last, cut


def edgeConnectivity(G, V):
    res = float("inf")
    for _ in range(V - 1):
        last, prev_last, cut = minimumCutPhase(G)
        mergeVertices(G, last, prev_last)
        res = min(res, cut)
    return res


if __name__ == "__main__":
    mypath = "lab3\\graphs-lab3"
    for file in listdir(mypath):
        V, L = loadWeightedGraph(join(mypath, file))
        G = [Node() for _ in range(V + 1)]
        for u, v, c in L:
            G[u].addEdge(v, c)
            G[v].addEdge(u, c)
    
        print(file, edgeConnectivity(G, V))