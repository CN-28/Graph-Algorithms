import sys
sys.path.append("")
from os import listdir
from os.path import join
from dimacs import *

def BS_DFS(V, L, s, t):
    G = [[] for _ in range(V + 1)]
    for u, v, c in L:
        G[u].append((v, c))
        G[v].append((u, c))
    
    L.sort(key = lambda x: x[2])

    def DFS(u, visited, min_weight):
        stack = []
        stack.append(u)
        res = float("inf")
        while stack:
            u = stack.pop()
            visited.add(u)
            if u == t:
                return True

            for v, c in G[u]:
                if v not in visited and c >= min_weight:
                    stack.append(v)

    mid = 0
    l = 0
    r = len(L) - 1
    while l <= r:
        mid = (l + r) // 2
        visited = set()
        if DFS(s, visited, L[mid][2]):
            l = mid + 1
        else:
            r = mid - 1

    return L[r][2]
    
    
mypath = "lab1\graphs"
for file in listdir(mypath):
    V, L = loadWeightedGraph(join(mypath, file))
    print(file, BS_DFS(V, L, 1, 2))