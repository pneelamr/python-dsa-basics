# Articulation Points & Bridges: Vertices/edges whose removal increases the number of connected components.
# Found via DFS using discovery time and low values; a vertex u is an articulation point if a child v has low[v] >= disc[u].
# Bridges satisfy low[v] > disc[u] — no back-edge from v's subtree reaches u or above.

# Time: O(V + E) — single DFS pass visiting every vertex and edge once
# Space: O(V) — disc, low, parent, visited arrays all size V
def find_articulation_points(graph):
    disc = {}
    low = {}
    parent = {}
    visited = set()
    ap = set()
    timer = [0]

    def dfs(u):
        visited.add(u)
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        child_count = 0

        for v in graph.get(u, []):
            if v not in visited:
                child_count += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent.get(u) is None and child_count > 1:
                    ap.add(u)
                if parent.get(u) is not None and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)

    return ap

# Time: O(V + E) — single DFS pass visiting every vertex and edge once
# Space: O(V) — disc, low, parent, visited arrays all size V
def find_bridges(graph):
    disc = {}
    low = {}
    parent = {}
    visited = set()
    bridges = []
    timer = [0]

    def dfs(u):
        visited.add(u)
        disc[u] = low[u] = timer[0]
        timer[0] += 1

        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent.get(u):
                low[u] = min(low[u], disc[v])

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)

    return bridges
