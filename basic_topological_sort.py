# Topological Sort: Linear ordering of vertices in a Directed Acyclic Graph (DAG).
# Every directed edge u→v has u appearing before v in the ordering.
# Implemented via DFS post-order (reverse finish time) and Kahn's BFS algorithm.

# Time: O(V+E) — visits each vertex and edge exactly once
# Space: O(V) — visited set and stack/queue each store at most V vertices
def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]


def topological_sort_kahn(graph):
    in_degree = {v: 0 for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    queue = [v for v in graph if in_degree[v] == 0]
    order = []

    while queue:
        vertex = queue.pop(0)
        order.append(vertex)
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph):
        return []  # cycle detected

    return order
