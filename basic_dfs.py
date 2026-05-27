def dfs(graph, start):
    visited = []
    seen = set()
    _dfs_helper(graph, start, seen, visited)
    return visited


def _dfs_helper(graph, vertex, seen, visited):
    seen.add(vertex)
    visited.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in seen:
            _dfs_helper(graph, neighbor, seen, visited)


def dfs_iterative(graph, start):
    visited = []
    seen = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in seen:
            seen.add(vertex)
            visited.append(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in seen:
                    stack.append(neighbor)

    return visited


def dfs_path(graph, start, target):
    seen = set()

    def _find(vertex, path):
        if vertex == target:
            return path
        seen.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                result = _find(neighbor, path + [neighbor])
                if result:
                    return result
        return []

    return _find(start, [start])


def has_cycle(graph):
    seen = set()

    def _detect(vertex, parent):
        seen.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                if _detect(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in seen:
            if _detect(vertex, None):
                return True
    return False
