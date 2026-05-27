# Catalan Numbers: Sequence counting many combinatorial structures: valid bracket sequences, BST shapes, polygon triangulations.
# C(n) = (2n choose n) / (n+1) = sum of C(i)*C(n-1-i) for i in 0..n-1.
# Applications include counting the number of distinct binary trees with n+1 leaves and non-crossing partitions.

# Time: O(4^n / n^(3/2)) — exponential due to overlapping subproblems recomputed naively
# Space: O(n) — recursion stack depth up to n
def catalan_recursive(n):
    if n <= 1:
        return 1
    result = 0
    for i in range(n):
        result += catalan_recursive(i) * catalan_recursive(n - 1 - i)
    return result

# Time: O(n^2) — two nested loops: outer over n values, inner over i in 0..k-1
# Space: O(n) — DP table of size n+1
def catalan_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for k in range(2, n + 1):
        for i in range(k):
            dp[k] += dp[i] * dp[k - 1 - i]
    return dp[n]

# Time: O(n) — compute (2n choose n) incrementally then divide by n+1
# Space: O(1) — constant extra space
def catalan_formula(n):
    result = 1
    for i in range(n):
        result = result * (2 * n - i) // (i + 1)
    return result // (n + 1)

# Time: O(n^2) — builds DP table of size n+1 using catalan_dp logic
# Space: O(n) — stores all n+1 Catalan numbers
def catalan_sequence(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for k in range(2, n + 1):
        for i in range(k):
            dp[k] += dp[i] * dp[k - 1 - i]
    return dp
