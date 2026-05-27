import bisect


# Time: O(2^n) — each element either included or excluded with no caching
# Space: O(n) — call stack depth
def lis_recursive(arr, prev, curr):
    if curr == len(arr):
        return 0
    exclude = lis_recursive(arr, prev, curr + 1)
    include = 0
    if prev == -1 or arr[curr] > arr[prev]:
        include = 1 + lis_recursive(arr, curr, curr + 1)
    return max(include, exclude)


# Time: O(n²) — double nested loop comparing each pair of elements
# Space: O(n) — dp and parent arrays of size n
def lis_tabulation(arr):
    n = len(arr)
    if not arr:
        return 0, []

    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    max_len = max(dp)
    idx = dp.index(max_len)

    sequence = []
    while idx != -1:
        sequence.append(arr[idx])
        idx = parent[idx]

    return max_len, sequence[::-1]


# Time: O(n log n) — binary search on tails array for each of n elements
# Space: O(n) — tails array stores at most n elements
def lis_optimized(arr):
    tails = []
    for val in arr:
        pos = bisect.bisect_left(tails, val)
        if pos == len(tails):
            tails.append(val)
        else:
            tails[pos] = val
    return len(tails)
