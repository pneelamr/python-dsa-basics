# Time: O(M^V) — M colors, V vertices
# Space: O(V) — color array and recursion stack

def graph_coloring(graph, num_colors):
    vertices = list(graph.keys())
    colors = {v: 0 for v in vertices}

    if _solve(graph, vertices, num_colors, colors, 0):
        return colors
    return {}


def _solve(graph, vertices, num_colors, colors, idx):
    if idx == len(vertices):
        return True

    vertex = vertices[idx]
    for color in range(1, num_colors + 1):
        if _is_safe(graph, vertex, color, colors):
            colors[vertex] = color
            if _solve(graph, vertices, num_colors, colors, idx + 1):
                return True
            colors[vertex] = 0

    return False


def _is_safe(graph, vertex, color, colors):
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True


def display(colors):
    for vertex, color in colors.items():
        print(f'  {vertex}: color {color}')
