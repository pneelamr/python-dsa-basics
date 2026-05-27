# Tarjan's SCC: Finds all Strongly Connected Components in a directed graph using a single DFS pass.
# Assigns each node a discovery time and low-link value; a node is an SCC root when disc[u] == low[u].
# A stack tracks the current DFS path; when an SCC root is found, all nodes on the stack down to it form that SCC.

# Time: O(V + E) — each node and edge visited exactly once in DFS
# Space: O(V) — disc, low, on_stack arrays and the DFS stack all size V
def tarjan_scc(graph):
    disc = {}
    low = {}
    on_stack = {}
    stack = []
    sccs = []
    timer = [0]

    def dfs(u):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        stack.append(u)
        on_stack[u] = True

        for v in graph.get(u, []):
            if v not in disc:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack.get(v, False):
                low[u] = min(low[u], disc[v])

        if low[u] == disc[u]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == u:
                    break
            sccs.append(scc)

    for node in graph:
        if node not in disc:
            dfs(node)

    return sccs
