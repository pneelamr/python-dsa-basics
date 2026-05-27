# Kruskal's Algorithm: Greedy minimum spanning tree algorithm for undirected weighted graphs.
# Sorts all edges by weight and adds each edge if it doesn't form a cycle (checked with Union-Find).
# O(E log E) time; works well for sparse graphs.

# Time: O(E log E) — dominated by sorting edges; union-find ops are near O(1)
# Space: O(V+E) — parent/rank dicts for V vertices, sorted edge list for E edges
def kruskal(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True

    mst = []
    total_cost = 0

    for weight, u, v in sorted(edges):
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost
