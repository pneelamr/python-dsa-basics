# Time: O(2^n) — each element either included or excluded without caching
# Space: O(n) — call stack depth bounded by number of elements
def subset_sum_recursive(arr, n, target):
    if target == 0:
        return True
    if n == 0:
        return False
    if arr[n - 1] > target:
        return subset_sum_recursive(arr, n - 1, target)
    return (subset_sum_recursive(arr, n - 1, target) or
            subset_sum_recursive(arr, n - 1, target - arr[n - 1]))


# Time: O(n*target) — at most n*target unique (n, target) subproblems cached
# Space: O(n*target) — memo dict plus O(n) call stack
def subset_sum_memoization(arr, n, target, memo=None):
    if memo is None:
        memo = {}
    if target == 0:
        return True
    if n == 0:
        return False
    if (n, target) in memo:
        return memo[(n, target)]
    if arr[n - 1] > target:
        memo[(n, target)] = subset_sum_memoization(arr, n - 1, target, memo)
    else:
        memo[(n, target)] = (subset_sum_memoization(arr, n - 1, target, memo) or
                             subset_sum_memoization(arr, n - 1, target - arr[n - 1], memo))
    return memo[(n, target)]


# Time: O(n*target) — fills (n+1)×(target+1) dp table
# Space: O(n*target) — dp table of size (n+1)×(target+1)
def subset_sum_tabulation(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    if not dp[n][target]:
        return False, []

    subset = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append(arr[i - 1])
            j -= arr[i - 1]
        i -= 1

    return True, subset[::-1]
