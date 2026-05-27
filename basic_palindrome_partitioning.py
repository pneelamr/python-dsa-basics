# Palindrome Partitioning: Split a string into the fewest parts such that every part is a palindrome.
# DP pre-computes which substrings are palindromes; a second DP finds the minimum cuts.
# O(n²) time and space; backtracking variant enumerates all valid partitions.

def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


# Time: O(2^n) — exponential branching over partition positions without caching
# Space: O(n) — call stack depth bounded by string length
def palindrome_partition_recursive(s, i, j):
    if i >= j or is_palindrome(s, i, j):
        return 0
    min_cuts = float('inf')
    for k in range(i, j):
        if is_palindrome(s, i, k):
            cuts = 1 + palindrome_partition_recursive(s, k + 1, j)
            min_cuts = min(min_cuts, cuts)
    return min_cuts


# Time: O(n²) — n² subproblems with palindrome check per split (amortized)
# Space: O(n²) — memo dict plus O(n) call stack
def palindrome_partition_memoization(s, i, j, memo=None):
    if memo is None:
        memo = {}
    if i >= j or is_palindrome(s, i, j):
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    min_cuts = float('inf')
    for k in range(i, j):
        if is_palindrome(s, i, k):
            cuts = 1 + palindrome_partition_memoization(s, k + 1, j, memo)
            min_cuts = min(min_cuts, cuts)
    memo[(i, j)] = min_cuts
    return memo[(i, j)]


# Time: O(n²) — precomputes palindrome table in O(n²) then fills dp in O(n²)
# Space: O(n²) — palindrome table plus O(n) dp array
def palindrome_partition_tabulation(s):
    n = len(s)

    # precompute palindrome table
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                pal[i][j] = s[i] == s[j]
            else:
                pal[i][j] = s[i] == s[j] and pal[i + 1][j - 1]

    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        if pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if pal[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1

    # reconstruct partitions
    parts = []
    i = n - 1
    while i >= 0:
        for j in range(i, -1, -1):
            if pal[j][i] and (j == 0 or dp[j - 1] == dp[i] - 1):
                parts.append(s[j:i + 1])
                i = j - 1
                break

    return dp[n - 1], parts[::-1]
