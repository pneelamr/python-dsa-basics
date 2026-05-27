# Kosaraju's SCC: Finds Strongly Connected Components using two DFS passes on the original and transposed graph.
# First DFS records finish order; second DFS on transposed graph in reverse finish order identifies SCCs.
# Conceptually simpler than Tarjan's; both run in O(V+E) but Kosaraju traverses the graph twice.

# Time: O(V + E) — two full DFS passes, each visiting all nodes and edges once
# Space: O(V + E) — transposed graph, visited set, finish order stack, all O(V+E)
def kosaraju_scc(graph):
    visited = set()
    finish_order = []

    def dfs1(u):
        stack = [(u, iter(graph.get(u, [])))]
        visited.add(u)
        while stack:
            node, neighbors = stack[-1]
            try:
                v = next(neighbors)
                if v not in visited:
                    visited.add(v)
                    stack.append((v, iter(graph.get(v, []))))
            except StopIteration:
                finish_order.append(node)
                stack.pop()

    for node in graph:
        if node not in visited:
            dfs1(node)

    transposed = {}
    for u in graph:
        if u not in transposed:
            transposed[u] = []
        for v in graph.get(u, []):
            if v not in transposed:
                transposed[v] = []
            transposed[v].append(u)

    visited2 = set()
    sccs = []

    def dfs2(u):
        stack = [u]
        visited2.add(u)
        scc = []
        while stack:
            node = stack.pop()
            scc.append(node)
            for v in transposed.get(node, []):
                if v not in visited2:
                    visited2.add(v)
                    stack.append(v)
        return scc

    for node in reversed(finish_order):
        if node not in visited2:
            sccs.append(dfs2(node))

    return sccs
