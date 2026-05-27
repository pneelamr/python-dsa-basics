# Longest Common Subsequence (LCS): Find the longest sequence of characters present in both strings in the same relative order.
# Solved with a 2D DP table where dp[i][j] = LCS length of s1[:i] and s2[:j].
# O(m × n) time and space; the actual subsequence is recovered by tracing back through the table.

# Time: O(2^(m+n)) — exponential branching with no caching
# Space: O(m+n) — call stack depth bounded by sum of string lengths
def lcs_recursive(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs_recursive(s1, s2, m - 1, n - 1)
    return max(lcs_recursive(s1, s2, m - 1, n), lcs_recursive(s1, s2, m, n - 1))


# Time: O(m*n) — at most m*n unique (m, n) subproblems cached
# Space: O(m*n) — memo dict plus O(m+n) call stack
def lcs_memoization(s1, s2, m, n, memo=None):
    if memo is None:
        memo = {}
    if m == 0 or n == 0:
        return 0
    if (m, n) in memo:
        return memo[(m, n)]
    if s1[m - 1] == s2[n - 1]:
        memo[(m, n)] = 1 + lcs_memoization(s1, s2, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs_memoization(s1, s2, m - 1, n, memo),
                           lcs_memoization(s1, s2, m, n - 1, memo))
    return memo[(m, n)]


# Time: O(m*n) — fills (m+1)×(n+1) dp table
# Space: O(m*n) — dp table of size (m+1)×(n+1)
def lcs_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # reconstruct the LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j += -1

    return dp[m][n], ''.join(reversed(lcs))
