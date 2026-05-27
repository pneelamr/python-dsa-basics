# Rod Cutting: Given a rod of length n and prices for each length, find the maximum revenue from cuts.
# Solved with bottom-up DP — dp[i] = max revenue for a rod of length i.
# O(n²) time; a variant of the unbounded knapsack problem.

# Time: O(2^n) — tries all cut combinations without caching
# Space: O(n) — call stack depth bounded by rod length
def rod_cut_recursive(prices, n):
    if n == 0:
        return 0
    max_val = float('-inf')
    for i in range(1, n + 1):
        max_val = max(max_val, prices[i - 1] + rod_cut_recursive(prices, n - i))
    return max_val


# Time: O(n²) — at most n subproblems each trying up to n cut sizes
# Space: O(n) — memo dict plus O(n) call stack
def rod_cut_memoization(prices, n, memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    max_val = float('-inf')
    for i in range(1, n + 1):
        max_val = max(max_val, prices[i - 1] + rod_cut_memoization(prices, n - i, memo))
    memo[n] = max_val
    return memo[n]


# Time: O(n²) — fills dp array of size n+1, trying up to n cut sizes each
# Space: O(n) — dp and cuts arrays of size n+1
def rod_cut_tabulation(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)

    for length in range(1, n + 1):
        max_val = float('-inf')
        for i in range(1, length + 1):
            if prices[i - 1] + dp[length - i] > max_val:
                max_val = prices[i - 1] + dp[length - i]
                cuts[length] = i
        dp[length] = max_val

    # reconstruct cut sizes
    pieces = []
    remaining = n
    while remaining > 0:
        pieces.append(cuts[remaining])
        remaining -= cuts[remaining]

    return dp[n], pieces
