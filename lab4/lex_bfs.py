def lexBFS(G, u):
    subsets = [set(), set()]
    V = {s for s in range(1, len(G)) if s != u}
    
    for v in G[u].out:
        subsets[1].add(v)
    
    visit_order = [u]
    subsets[0] = V - subsets[1]
    while subsets:
        u = subsets[-1].pop()
        visit_order.append(u)

        new_subsets = []
        for X in subsets:
            Y = set()
            K = set()

            for v in X:
                if v in G[u].out:
                    Y.add(v)
                else:
                    K.add(v)
                
            if K:
                new_subsets.append(K)
            if Y:
                new_subsets.append(Y)
        
        subsets = new_subsets
    
    return visit_order