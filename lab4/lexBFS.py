def lexBFS(G, u):
    subsets = [set(), set()]
    V = {s for s in range(1, len(G))}
    
    visited = {u}
    for v in G[u].out:
        subsets[1].add(v)
    
    subsets[0] = V - subsets[1]

