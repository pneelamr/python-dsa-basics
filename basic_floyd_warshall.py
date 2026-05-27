# Floyd-Warshall: All-pairs shortest-path algorithm using dynamic programming.
# Considers every vertex k as an intermediate node and relaxes paths through it.
# O(V³) time and O(V²) space; handles negative edges but not negative cycles.

# Time: O(V³) — three nested loops each iterating over V vertices
# Space: O(V²) — distance and next_vertex matrices of size V×V
def floyd_warshall(graph):
    vertices = list(graph.keys())
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}

    dist = [[float('inf')] * n for _ in range(n)]
    next_vertex = [[None] * n for _ in range(n)]

    for v in vertices:
        dist[idx[v]][idx[v]] = 0

    for u in graph:
        for v, weight in graph[u]:
            dist[idx[u]][idx[v]] = weight
            next_vertex[idx[u]][idx[v]] = v

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]

    return dist, next_vertex, vertices


def shortest_path(dist, next_vertex, vertices, start, target):
    idx = {v: i for i, v in enumerate(vertices)}
    i, j = idx[start], idx[target]

    if dist[i][j] == float('inf'):
        return [], float('inf')

    path = [start]
    while path[-1] != target:
        path.append(next_vertex[idx[path[-1]]][j])

    return path, dist[i][j]


def display(dist, vertices):
    print('     ' + '  '.join(f'{v:>4}' for v in vertices))
    for i, u in enumerate(vertices):
        row = '  '.join('  inf' if d == float('inf') else f'{d:>4}' for d in dist[i])
        print(f'{u:>4} {row}')
