from data import runtests
from collections import deque
from time import time

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
    F = [{} for _ in range(V + 1)]
    
    relabel_to_front(G, F, 0, V, V)
    for u in range(V + 1):
        for v in G[u]:
            F[u][v] = G[u][v] - F[u][v]
    while True:
        i, cycle = Bellman_Ford(F, 1, weights, k)
        if not cycle:
            break

        for a, b in cycle:
            F[a][b] -= i
            F[b][a] += i

    res = 0
    for u in range(1, V + 1):
        for v in F[u]:
            if u < v:
                if F[v][u] > 0:
                    res += weights[u][v][F[v][u] - 1]

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


def Bellman_Ford(G, s, weights, k):
    n = len(G)
    dist = [float("inf")] * n
    parent = [-1] * n

    dist[s] = 0
    for _ in range(n - 2):
        for u in range(1, n):
            for v in G[u]:
                if v == 0:
                    continue
                if u < v:
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
            if u < v:
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

                #add checking sum of cycles
                for i in range(k):
                    suum = 0
                    for w, z in cycle:
                        if w < z:
                            if 0 < G[z][w] + i < len(weights[w][z]):
                                c = weights[w][z][G[z][w] + i] - weights[w][z][G[z][w] - 1 + i]
                            elif G[z][w] + i == 0:
                                c = weights[w][z][G[z][w] + i]
                            else:
                                return i, cycle
                        else:
                            if G[w][z] - 2 - i >= 0:
                                c = -(weights[z][w][G[w][z] - 1 - i] - weights[z][w][G[w][z] - 2 - i])
                            elif G[w][z] - 1 - i == 0:
                                c = -(weights[z][w][G[w][z] - 1 - i])
                            else:
                                return i, cycle
                        
                        suum += c
                    if suum >= 0:
                        return i, cycle
    return -1, False



def relabel_to_front(G, F, source, sink, n):
    n = len(G)
    for u in range(n):
        for v in G[u]:
            F[u][v] = 0

    height = [0] * n
    excess = [0] * n
   
    nodelist = deque([i for i in range(1, n - 1)])
    
    def push(u, v):
        send = min(excess[u], G[u][v] - F[u][v])
        F[u][v] += send
        F[v][u] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        min_height = float("inf")
        for v in G[u]:
            if G[u][v] - F[u][v] > 0:
                min_height = min(min_height, height[v])
                height[u] = min_height + 1

    def discharge(u):
        while excess[u] > 0:
            for v in G[u]:
                if G[u][v] - F[u][v] > 0 and height[u] > height[v]:
                    push(u, v)
              
            relabel(u)
 

    height[source] = n
    excess[source] = float("inf")
    for v in G[source]:
        push(source, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            x = nodelist[p]
            nodelist.remove(x)
            nodelist.appendleft(x)
            p = 0
        else:
            p += 1


runtests(my_solve)