import sys
from maxFlow import maxFlow, bfs
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join
from copy import deepcopy


if __name__ == "__main__":
    mypath = "lab2\\graphs-lab2\\connectivity"
    for file in listdir(mypath):
        V, L = loadWeightedGraph(join(mypath, file))
        G = {}
        for u in range(1, V + 1):
            G[u] = {}
        
        for u, v, w in L:
            G[u][v] = w
            G[v][u] = w
        
        mini = float("inf")
        for u in range(1, V):
            G1 = deepcopy(G)
            mini = min(mini, maxFlow(G1, V, u, V, bfs))
            
        print(file, mini)