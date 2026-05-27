# Time: O(2^n) — each call branches into two recursive calls with no caching
# Space: O(n) — call stack depth reaches n
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Time: O(n) — each subproblem computed once and cached
# Space: O(n) — memo dict stores n results plus O(n) call stack
def fibonacci_memoization(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


# Time: O(n) — single pass filling dp table
# Space: O(n) — dp array of size n+1
def fibonacci_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Time: O(n) — single pass with two rolling variables
# Space: O(1) — only two variables needed regardless of n
def fibonacci_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
