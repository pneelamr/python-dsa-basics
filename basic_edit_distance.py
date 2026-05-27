def edit_distance_recursive(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        return edit_distance_recursive(s1, s2, m - 1, n - 1)
    insert  = edit_distance_recursive(s1, s2, m, n - 1)
    delete  = edit_distance_recursive(s1, s2, m - 1, n)
    replace = edit_distance_recursive(s1, s2, m - 1, n - 1)
    return 1 + min(insert, delete, replace)


def edit_distance_memoization(s1, s2, m, n, memo=None):
    if memo is None:
        memo = {}
    if m == 0:
        return n
    if n == 0:
        return m
    if (m, n) in memo:
        return memo[(m, n)]
    if s1[m - 1] == s2[n - 1]:
        memo[(m, n)] = edit_distance_memoization(s1, s2, m - 1, n - 1, memo)
    else:
        insert  = edit_distance_memoization(s1, s2, m, n - 1, memo)
        delete  = edit_distance_memoization(s1, s2, m - 1, n, memo)
        replace = edit_distance_memoization(s1, s2, m - 1, n - 1, memo)
        memo[(m, n)] = 1 + min(insert, delete, replace)
    return memo[(m, n)]


def edit_distance_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],       # insert
                                    dp[i - 1][j],        # delete
                                    dp[i - 1][j - 1])    # replace

    # reconstruct operations
    ops = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            ops.append(f"insert '{s2[j - 1]}' at {i}")
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            ops.append(f"delete '{s1[i - 1]}' at {i - 1}")
            i -= 1
        else:
            ops.append(f"replace '{s1[i - 1]}' → '{s2[j - 1]}' at {i - 1}")
            i -= 1
            j -= 1

    return dp[m][n], ops[::-1]
