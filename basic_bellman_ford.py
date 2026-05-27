# Time: O(V*E) — relaxes all E edges V-1 times
# Space: O(V) — distances and previous arrays store one entry per vertex
def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}

    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((vertex, neighbor, weight))

    for _ in range(len(graph) - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                previous[v] = u

    for u, v, weight in edges:
        if distances[u] + weight < distances[v]:
            return None, None  # negative cycle detected

    return distances, previous


def shortest_path(graph, start, target):
    distances, previous = bellman_ford(graph, start)

    if distances is None:
        return [], float('-inf')  # negative cycle

    if distances[target] == float('inf'):
        return [], float('inf')  # unreachable

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1], distances[target]
