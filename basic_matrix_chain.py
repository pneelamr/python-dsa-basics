# Time: O(2^n) — exponential branching over split points without caching
# Space: O(n) — call stack depth bounded by number of matrices
def matrix_chain_recursive(dims, i, j):
    if i == j:
        return 0
    min_cost = float('inf')
    for k in range(i, j):
        cost = (matrix_chain_recursive(dims, i, k) +
                matrix_chain_recursive(dims, k + 1, j) +
                dims[i - 1] * dims[k] * dims[j])
        min_cost = min(min_cost, cost)
    return min_cost


# Time: O(n³) — n² subproblems each trying up to n split points
# Space: O(n²) — memo dict plus O(n) call stack
def matrix_chain_memoization(dims, i, j, memo=None):
    if memo is None:
        memo = {}
    if i == j:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    min_cost = float('inf')
    for k in range(i, j):
        cost = (matrix_chain_memoization(dims, i, k, memo) +
                matrix_chain_memoization(dims, k + 1, j, memo) +
                dims[i - 1] * dims[k] * dims[j])
        min_cost = min(min_cost, cost)
    memo[(i, j)] = min_cost
    return memo[(i, j)]


# Time: O(n³) — three nested loops over chain lengths, start positions, and split points
# Space: O(n²) — dp and split tables of size (n+1)×(n+1)
def matrix_chain_tabulation(dims):
    n = len(dims) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp[1][n], _get_order(split, 1, n)


def _get_order(split, i, j):
    if i == j:
        return f'M{i}'
    k = split[i][j]
    left = _get_order(split, i, k)
    right = _get_order(split, k + 1, j)
    return f'({left} x {right})'
