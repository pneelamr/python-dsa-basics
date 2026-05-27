# Dijkstra's Algorithm: Greedy shortest-path algorithm for weighted graphs with non-negative edge weights.
# Uses a min-heap priority queue to always expand the lowest-cost unvisited node.
# O((V + E) log V) with a binary heap; does not handle negative edge weights.

import heapq


# Time: O((V+E) log V) — each edge relaxation may push to heap, heap ops are O(log V)
# Space: O(V) — distances, previous, and heap each store at most V entries
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
