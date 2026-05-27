# Eulerian Path & Circuit: A path/circuit traversing every edge exactly once (Eulerian) found via Hierholzer's algorithm.
# Eulerian circuit exists iff all vertices have even degree; Eulerian path exists iff exactly 0 or 2 vertices have odd degree.
# Hierholzer's starts at a valid vertex, follows edges (removing them), and splices sub-tours when stuck. O(E).

import collections

# Time: O(V + E) — compute degree of every vertex
# Space: O(V) — degree dictionary
def has_eulerian_circuit(graph):
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return False
    return True

# Time: O(V + E) — count vertices with odd degree
# Space: O(V) — degree dictionary
def has_eulerian_path(graph):
    odd = sum(1 for node in graph if len(graph[node]) % 2 != 0)
    return odd == 0 or odd == 2

# Time: O(E) — Hierholzer's algorithm visits each edge exactly once
# Space: O(E) — adjacency lists (copy) and result path
def eulerian_circuit(graph):
    adj = {u: collections.deque(neighbors) for u, neighbors in graph.items()}
    start = next(iter(adj))
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if adj[v]:
            u = adj[v].popleft()
            if u in adj:
                adj[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    path.reverse()
    return path

# Time: O(E) — Hierholzer's algorithm visits each edge exactly once
# Space: O(E) — adjacency lists (copy) and result path
def eulerian_path(graph):
    odd_nodes = [node for node in graph if len(graph[node]) % 2 != 0]
    odd_count = len(odd_nodes)
    if odd_count != 0 and odd_count != 2:
        return []
    adj = {u: collections.deque(neighbors) for u, neighbors in graph.items()}
    start = odd_nodes[0] if odd_count == 2 else next(iter(adj))
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if adj[v]:
            u = adj[v].popleft()
            if u in adj:
                try:
                    adj[u].remove(v)
                except ValueError:
                    pass
            stack.append(u)
        else:
            path.append(stack.pop())
    path.reverse()
    return path
