# A* Search: Heuristic shortest-path algorithm combining actual path cost g(n) and estimated cost h(n).
# Expands the node with the lowest f(n) = g(n) + h(n) using a min-heap.
# With an admissible heuristic, always finds the optimal path; here Manhattan distance is used.

import heapq


# Time: O((V+E) log V) — like Dijkstra but guided by heuristic; heap ops are O(log V)
# Space: O(V) — g_score, f_score, previous, and open_set each store at most V entries
def a_star(graph, start, target, heuristic):
    open_set = [(0, start)]
    g_score = {vertex: float('inf') for vertex in graph}
    g_score[start] = 0
    f_score = {vertex: float('inf') for vertex in graph}
    f_score[start] = heuristic(start, target)
    previous = {vertex: None for vertex in graph}

    while open_set:
        _, vertex = heapq.heappop(open_set)

        if vertex == target:
            return _reconstruct_path(previous, target), g_score[target]

        for neighbor, weight in graph[vertex]:
            tentative_g = g_score[vertex] + weight
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, target)
                previous[neighbor] = vertex
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return [], float('inf')


def _reconstruct_path(previous, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1]
