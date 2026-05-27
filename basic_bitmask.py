# Bitmask: Represent subsets of n elements as integers where bit i = 1 means element i is included.
# Enumerate all 2^n subsets; apply bitwise AND/OR to compute set intersections and unions in O(1).
# Bitmask DP compresses exponential state spaces — e.g., Travelling Salesman Problem in O(2^n * n²).

# Time: O(2^n * n) — iterate over all 2^n masks, each decoded in O(n)
# Space: O(2^n * n) — store all subsets
def enumerate_subsets(arr):
    n = len(arr)
    subsets = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        subsets.append(subset)
    return subsets

# Time: O(2^n * n) — iterate over all 2^n masks and decode each in O(n)
# Space: O(2^n * n) — store matching subsets
def subset_sum_bitmask(arr, target):
    n = len(arr)
    result = []
    for mask in range(1 << n):
        subset = []
        total = 0
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
                total += arr[i]
        if total == target:
            result.append(subset)
    return result

# Time: O(2^n * n^2) — outer loop over 2^n masks, inner loop over n nodes, transition over n predecessors
# Space: O(2^n * n) — DP table indexed by (mask, last_node)
def tsp_bitmask(dist):
    n = len(dist)
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
    full_mask = (1 << n) - 1
    best = INF
    for u in range(1, n):
        if dp[full_mask][u] + dist[u][0] < best:
            best = dp[full_mask][u] + dist[u][0]
    return best
