# Time: O(amount^coins) — exponential branching without memoization
# Space: O(amount) — call stack depth bounded by amount
def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    min_coins = float('inf')
    for coin in coins:
        result = coin_change_recursive(coins, amount - coin)
        if result != float('inf'):
            min_coins = min(min_coins, 1 + result)
    return min_coins


# Time: O(amount*coins) — each amount computed once across all coins
# Space: O(amount) — memo dict plus O(amount) call stack
def coin_change_memoization(coins, amount, memo=None):
    if memo is None:
        memo = {}
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    if amount in memo:
        return memo[amount]
    min_coins = float('inf')
    for coin in coins:
        result = coin_change_memoization(coins, amount - coin, memo)
        if result != float('inf'):
            min_coins = min(min_coins, 1 + result)
    memo[amount] = min_coins
    return memo[amount]


# Time: O(amount*coins) — fills dp array of size amount+1, checking each coin
# Space: O(amount) — dp array of size amount+1
def coin_change_tabulation(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    if dp[amount] == float('inf'):
        return -1, []

    # reconstruct coins used
    used = []
    remaining = amount
    while remaining > 0:
        for coin in coins:
            if coin <= remaining and dp[remaining - coin] == dp[remaining] - 1:
                used.append(coin)
                remaining -= coin
                break

    return dp[amount], used
