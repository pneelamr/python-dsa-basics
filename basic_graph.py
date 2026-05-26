def create_graph():
    return {}


def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []


def add_edge(graph, v1, v2):
    add_vertex(graph, v1)
    add_vertex(graph, v2)
    graph[v1].append(v2)
    graph[v2].append(v1)


def remove_edge(graph, v1, v2):
    graph[v1].remove(v2)
    graph[v2].remove(v1)


def remove_vertex(graph, vertex):
    for neighbor in graph[vertex]:
        graph[neighbor].remove(vertex)
    del graph[vertex]


def bfs(graph, start):
    visited = []
    queue = [start]
    seen = {start}
    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return visited


def dfs(graph, start, seen=None):
    if seen is None:
        seen = set()
    seen.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in seen:
            result += dfs(graph, neighbor, seen)
    return result


def display(graph):
    for vertex, neighbors in graph.items():
        print(f"{vertex} -> {neighbors}")
