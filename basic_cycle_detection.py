# Cycle Detection: Floyd's tortoise-and-hare finds cycles in a sequence f(x) using two pointers at different speeds.
# Slow pointer advances one step; fast pointer advances two; if they meet, a cycle exists.
# After detection, resetting one pointer to start and advancing both one step at a time finds the cycle entry point.

# Time: O(lambda + mu) — lambda is cycle length, mu is distance to cycle start; at most 2*(mu+lambda) steps
# Space: O(1) — only two pointer variables regardless of sequence length
def floyd_detect(f, start):
    slow = f(start)
    fast = f(f(start))
    while slow != fast:
        slow = f(slow)
        fast = f(f(fast))
        if fast is None or slow is None:
            return False, None, None

    cycle_start_val = start
    slow2 = start
    while slow2 != slow:
        slow2 = f(slow2)
        slow = f(slow)
    cycle_start = slow2

    length = 1
    runner = f(cycle_start)
    while runner != cycle_start:
        runner = f(runner)
        length += 1

    return True, cycle_start, length

# Time: O(V + E) — DFS visits each vertex and edge once
# Space: O(V) — visited and recursion_stack sets both size V
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(u):
        visited.add(u)
        rec_stack.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                if dfs(v):
                    return True
            elif v in rec_stack:
                return True
        rec_stack.discard(u)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Time: O(V + E) — DFS visits each vertex and edge once
# Space: O(V) — visited dict (with parent) and recursion stack both size V
def has_cycle_undirected(graph):
    visited = {}

    def dfs(u, parent):
        visited[u] = True
        for v in graph.get(u, []):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
