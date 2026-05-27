import heapq


# Time: O((V+E) log V) — each edge may be pushed to heap; heap ops are O(log V)
# Space: O(V) — visited set, mst list, and heap each bounded by V or E entries
def prim(graph, start):
    visited = {start}
    mst = []
    total_cost = 0
    heap = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(heap)

    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)
        mst.append((u, v, weight))
        total_cost += weight

        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heapq.heappush(heap, (w, v, neighbor))

    return mst, total_cost
