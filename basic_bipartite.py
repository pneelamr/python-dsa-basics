# Bipartite Graph: A graph whose vertices can be 2-colored so no two adjacent vertices share the same color.
# Equivalently, a graph is bipartite if and only if it contains no odd-length cycles.
# BFS-based 2-coloring assigns alternating colors; if a conflict is found, the graph is not bipartite.

import collections

# Time: O(V + E) — BFS visits every vertex and edge once
# Space: O(V) — color array and BFS queue both size V
def is_bipartite(graph):
    color = {}
    for start in graph:
        if start in color:
            continue
        queue = collections.deque([start])
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in graph.get(u, []):
                if v not in color:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
    return True

# Time: O(V + E) — BFS visits every vertex and edge once
# Space: O(V) — color dictionary and BFS queue both size V
def bipartite_coloring(graph):
    color = {}
    for start in graph:
        if start in color:
            continue
        queue = collections.deque([start])
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in graph.get(u, []):
                if v not in color:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return {}
    return color
