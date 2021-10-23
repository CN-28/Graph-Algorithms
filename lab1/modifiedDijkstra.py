from dimacs import *
from queue import PriorityQueue
from os import listdir
from os.path import join

def modifiedDijkstra(V, L, s, t):
    G = [[] for _ in range(V + 1)]
    weight = [0 for _ in range(V + 1)]
    Q = PriorityQueue()
    for u, v, cost in L:
        G[u].append((v, cost))
        G[v].append((u, cost))

    Q.put((-float("inf"), s))
    while not Q.empty():
        c, u = Q.get()
        if u == t:
            return weight[t]
        c = -c    
        for v, cost in G[u]:
            if min(c, cost) > weight[v]:
                weight[v] = min(c, cost)
                Q.put((-min(cost, c), v))


mypath = "lab1\graphs"
for file in listdir(mypath):
    V, L = loadWeightedGraph(join(mypath, file))
    print(file, modifiedDijkstra(V, L, 1, 2))