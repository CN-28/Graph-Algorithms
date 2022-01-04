import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join
import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort


def check_satisfiability(SCC):
    H = nx.DiGraph()
    t = 0
    for S in SCC:
        check = {}
        for v in S:
            check[v] = True
            if -v in check:
                return False
        t += 1

    return True



if __name__ == "__main__":
    mypath = "lab5\\sat"
    for file in listdir(mypath):
        print()
        print(file, end=" ")
        V, F = loadCNFFormula(join(mypath, file))
        G = nx.DiGraph()

        for var1, var2 in F:
            if not G.has_node(var1):
                G.add_node(var1)
            if not G.has_node(var2):
                G.add_node(var2)
            if not G.has_node(-var1):
                G.add_node(-var1)
            if not G.has_node(-var2):
                G.add_node(-var2)


            G.add_edge(-var1, var2)
            G.add_edge(-var2, var1)

        SCC = strongly_connected_components(G)
        satisfiable = check_satisfiability(SCC)
        print(satisfiable)
        if satisfiable:
            ...
            

