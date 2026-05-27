# Time: O(V!) — try every permutation of vertices
# Space: O(V) — path array and recursion stack

def hamiltonian_path(graph):
    vertices = list(graph.keys())
    for start in vertices:
        path = [start]
        visited = {start}
        if _solve(graph, vertices, path, visited):
            return path
    return []


def hamiltonian_cycle(graph):
    vertices = list(graph.keys())
    start = vertices[0]
    path = [start]
    visited = {start}
    if _solve_cycle(graph, vertices, path, visited, start):
        return path + [start]
    return []


def _solve(graph, vertices, path, visited):
    if len(path) == len(vertices):
        return True
    current = path[-1]
    for neighbor in graph[current]:
        if neighbor not in visited:
            path.append(neighbor)
            visited.add(neighbor)
            if _solve(graph, vertices, path, visited):
                return True
            path.pop()
            visited.remove(neighbor)
    return False


def _solve_cycle(graph, vertices, path, visited, start):
    if len(path) == len(vertices):
        return start in graph[path[-1]]
    current = path[-1]
    for neighbor in graph[current]:
        if neighbor not in visited:
            path.append(neighbor)
            visited.add(neighbor)
            if _solve_cycle(graph, vertices, path, visited, start):
                return True
            path.pop()
            visited.remove(neighbor)
    return False
