# Breadth-First Search (BFS): Graph traversal that explores all neighbors at the current depth before going deeper.
# Uses a queue to process nodes level by level; naturally finds shortest paths in unweighted graphs.
# Visits each vertex and edge once: O(V + E).

# Time: O(V+E) — each vertex and edge visited at most once
# Space: O(V) — visited list, seen set, and queue each hold at most V vertices
def bfs(graph, start):
    visited = []
    seen = {start}
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


def bfs_levels(graph, start):
    levels = {}
    seen = {start}
    queue = [start]
    level = 0

    while queue:
        next_queue = []
        for vertex in queue:
            levels[vertex] = level
            for neighbor in graph[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    next_queue.append(neighbor)
        queue = next_queue
        level += 1

    return levels


def bfs_path(graph, start, target):
    if start == target:
        return [start]

    seen = {start}
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                new_path = path + [neighbor]
                if neighbor == target:
                    return new_path
                seen.add(neighbor)
                queue.append(new_path)

    return []
