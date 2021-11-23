import sys
sys.path.append("")
from dimacs import *
from os import listdir
from os.path import join


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()

    def connect_to(self, v):
        self.out.add(v)


if __name__ == "__main__":
    mypath = ...
    for file in listdir(mypath):
        V, L = loadWeightedGraph(join(mypath, file))
        G = [None] + [Node(u) for u in range(1, V + 1)]

        for u, v, _ in L:
            G[u].connect_to(v)
            G[v].connect_to(u)
