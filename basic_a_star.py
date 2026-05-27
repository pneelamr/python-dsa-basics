import heapq


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
