import heapq


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    heap = [(0, start)]

    while heap:
        curr_dist, vertex = heapq.heappop(heap)

        if curr_dist > distances[vertex]:
            continue

        for neighbor, weight in graph[vertex]:
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                previous[neighbor] = vertex
                heapq.heappush(heap, (dist, neighbor))

    return distances, previous


def shortest_path(graph, start, target):
    distances, previous = dijkstra(graph, start)

    if distances[target] == float('inf'):
        return [], float('inf')

    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1], distances[target]
