def rod_cut_recursive(prices, n):
    if n == 0:
        return 0
    max_val = float('-inf')
    for i in range(1, n + 1):
        max_val = max(max_val, prices[i - 1] + rod_cut_recursive(prices, n - i))
    return max_val


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
