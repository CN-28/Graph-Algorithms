from data import runtests
from collections import deque

def my_solve(V, k, edges):
    print("Ilosc wierzcholkow: {}, krawedzi: {}".format(V, len(edges)))
    print("Ilosc oddzialow: {}".format(k))
    G = [{} for _ in range(V + 1)]
    weights = [{} for _ in range(V + 1)]

    for (a, b), losses in edges:
        weights[a][b] = losses
        G[a][b] = len(losses)
        G[b][a] = 0
    
    G[0][1] = k
    G[1][0] = 0
    max_flow = maxFlow(G, V, 0, V)
    while True:
        cycle = Bellman_Ford(G, 1, weights)
        if not cycle:
            break

        for a, b in cycle:
            G[a][b] -= 1
            G[b][a] += 1

    res = 0
    for u in range(V + 1):
        if u == 0:
            continue
        for v in G[u]:
            if v == 0:
                continue
            if v in weights[u]:
                if G[v][u] > 0:
                    res += weights[u][v][G[v][u] - 1]

    return res
    

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

    
def maxFlow(G, V, source, sink):
    parent = [-1] * (V + 1)
    max_flow = 0

    while bfs(G, source, sink, parent):
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


def Bellman_Ford(G, s, weights):
    n = len(G)
    dist = [float("inf")] * n
    parent = [-1] * n


    dist[s] = 0
    for _ in range(n - 2):
        for u in range(n):
            if u == 0:
                continue
            for v in G[u]:
                if v == 0:
                    continue
                if v in weights[u]:
                    if 0 < G[v][u] < len(weights[u][v]):
                        c = weights[u][v][G[v][u]] - weights[u][v][G[v][u] - 1]
                    elif G[v][u] == 0:
                        c = weights[u][v][G[v][u]]
                    else:
                        continue
                else:
                    if G[u][v] - 2 >= 0:
                        c = -(weights[v][u][G[u][v] - 1] - weights[v][u][G[u][v] - 2])
                    elif G[u][v] - 1 >= 0:
                        c = -(weights[v][u][G[u][v] - 1])
                    else:
                        continue

                if dist[u] + c < dist[v]:
                    dist[v] = dist[u] + c
                    parent[v] = u
    

    #check for negative-weight cycles
    for u in range(1, n):
        for v in G[u]:
            if v == 0:
                continue
            if v in weights[u]:
                if 0 < G[v][u] < len(weights[u][v]):
                    c = weights[u][v][G[v][u]] - weights[u][v][G[v][u] - 1]
                elif G[v][u] == 0:
                    c = weights[u][v][G[v][u]]
                else:
                    continue
            else:
                if G[u][v] - 2 >= 0:
                    c = -(weights[v][u][G[u][v] - 1] - weights[v][u][G[u][v] - 2])
                elif G[u][v] - 1 >= 0:
                    c = -(weights[v][u][G[u][v] - 1])
                else:
                    continue
            if dist[u] != float("inf") and dist[u] + c < dist[v]:
                temp = v
                cycle = []
                for _ in range(n):
                    temp = parent[temp]
                
                start = temp
                temp = parent[temp]
                while temp != start:
                    cycle.append((parent[temp], temp))
                    temp = parent[temp]
                cycle.append((parent[temp], temp))

                return cycle
                
    return False


runtests(my_solve)