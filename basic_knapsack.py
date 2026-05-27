# Time: O(2^n) — each item is either included or excluded with no caching
# Space: O(n) — recursive call stack depth
def knapsack_recursive(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack_recursive(weights, values, capacity, n - 1)
    include = values[n - 1] + knapsack_recursive(weights, values, capacity - weights[n - 1], n - 1)
    exclude = knapsack_recursive(weights, values, capacity, n - 1)
    return max(include, exclude)


# Time: O(n*W) — at most n*W unique (n, capacity) subproblems cached
# Space: O(n*W) — memo dict plus O(n) call stack
def knapsack_memoization(weights, values, capacity, n, memo=None):
    if memo is None:
        memo = {}
    if n == 0 or capacity == 0:
        return 0
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    if weights[n - 1] > capacity:
        memo[(n, capacity)] = knapsack_memoization(weights, values, capacity, n - 1, memo)
    else:
        include = values[n - 1] + knapsack_memoization(weights, values, capacity - weights[n - 1], n - 1, memo)
        exclude = knapsack_memoization(weights, values, capacity, n - 1, memo)
        memo[(n, capacity)] = max(include, exclude)
    return memo[(n, capacity)]


# Time: O(n*W) — fills (n+1)×(capacity+1) dp table
# Space: O(n*W) — dp table of size (n+1)×(W+1)
def knapsack_tabulation(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # reconstruct selected items
    items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], items[::-1]
