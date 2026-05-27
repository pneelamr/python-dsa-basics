def create(n):
    return {'matrix': [[0] * n for _ in range(n)], 'n': n}


# Time: O(1) add/remove/has_edge, O(V) neighbors — scans one full row
# Space: O(V²) — stores V×V matrix regardless of edge count
def add_edge(graph, u, v):
    graph['matrix'][u][v] = 1
    graph['matrix'][v][u] = 1


def remove_edge(graph, u, v):
    graph['matrix'][u][v] = 0
    graph['matrix'][v][u] = 0


def has_edge(graph, u, v):
    return graph['matrix'][u][v] == 1


def neighbors(graph, u):
    return [v for v in range(graph['n']) if graph['matrix'][u][v] == 1]


def display(graph):
    n = graph['n']
    print('  ' + ' '.join(str(i) for i in range(n)))
    for i in range(n):
        print(str(i) + ' ' + ' '.join(str(graph['matrix'][i][j]) for j in range(n)))
