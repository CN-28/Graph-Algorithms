import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join
from collections import deque
from copy import deepcopy

def bfs(G, s, t, parent):
    visited = set()
    Q = deque()

    Q.append(s)
    visited.add(s)
    while Q:
        u = Q.popleft()
        if u == t:
            return True
        for v in G[u]:
            if v not in visited and G[u][v] > 0:
                Q.append(v)
                visited.add(v)
                parent[v] = u 


def dfs(G, s, t, parent):
    visited = set()
    def dfsVisit(u):
        if u == t:
            return True

        visited.add(u)
        for v in G[u]:
            if v not in visited and G[u][v] > 0:
                parent[v] = u
                if dfsVisit(v):
                    return True

    return dfsVisit(s)


def maxFlow(G, V, source, sink, aug_path):
    parent = [-1 for _ in range(V + 1)]
    max_flow = 0

    while aug_path(G, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
        
    return max_flow


if __name__ == "__main__":
    mypath = "lab2\\graphs-lab2\\flow"
    for file in listdir(mypath):
        V, L = loadDirectedWeightedGraph(join(mypath, file))
        G = {}
        for u in range(1, V + 1):
            G[u] = {}
        
        for u, v, w in L:
            G[u][v] = w
            if u not in G[v]:
                G[v][u] = 0

        G1 = deepcopy(G)

        print(file, maxFlow(G, V, 1, V, dfs), maxFlow(G1, V, 1, V, dfs))