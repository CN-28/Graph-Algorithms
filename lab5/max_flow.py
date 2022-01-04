import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join
import networkx as nx
from networkx.algorithms.flow import maximum_flow


if __name__ == "__main__":
    mypath = "lab2\\graphs-lab2\\flow"
    for file in listdir(mypath):
        print(file, end=" ")
        V, L = loadDirectedWeightedGraph(join(mypath, file))

        G = nx.DiGraph()
        
        for u in range(1, V + 1):
            G.add_node(u)
        
        for u, v, capacity in L:
            G.add_edge(u, v)
            G[u][v]['capacity'] = capacity

        print(maximum_flow(G, 1, V)[0])