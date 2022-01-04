import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join
import networkx as nx
from networkx.algorithms.planarity import check_planarity



if __name__ == "__main__":
    mypath = "lab5\\graphs-lab7"
    for file in listdir(mypath):
        print(file)
        V, L = loadWeightedGraph(join(mypath, file))
        
        G = nx.Graph()
        for u in range(1, V + 1):
            G.add_node(u)

        for u, v, _ in L:
            G.add_edge(u, v)

        print(check_planarity(G))