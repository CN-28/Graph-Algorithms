from dimacs import *
from queue import PriorityQueue


def modifiedDijkstra(V, L, s, t):
    G = [[] for _ in range(V + 1)]
    dist = [0 for _ in range(V + 1)]
    Q = PriorityQueue()
    for u, v, cost in L:
        G[u].append((v, cost))
        G[v].append((u, cost))

    Q.put((-float("inf"), s))
    while not Q.empty():
        c, u = Q.get()
        c = -c    
        for v, cost in G[u]:
            if min(c, cost) > dist[v]:
                dist[v] = min(c, cost)
                Q.put((-min(cost, c), v))

    return dist[t]


V, L = loadWeightedGraph("lab1/graphs/rand1000_100000")
print(modifiedDijkstra(V, L, 1, 2))