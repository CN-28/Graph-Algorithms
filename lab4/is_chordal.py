def isChordal(G):
    parent = [-1 for _ in range(len(G))]
    RN = [set() for _ in range(len(G))]

    for v in G:
        ...