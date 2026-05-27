# Activity Selection: Greedy algorithm selecting the maximum number of non-overlapping activities.
# Sort activities by finish time; greedily pick each activity that starts at or after the last selected one ends.
# Optimal substructure: the earliest-finishing activity always belongs to some optimal solution.

# Time: O(n log n) — dominated by sorting; the greedy scan is O(n)
# Space: O(n) — output list holds at most n selected activities
def activity_selection(activities):
    sorted_acts = sorted(activities, key=lambda a: a[1])
    selected = []
    last_finish = float('-inf')
    for start, finish in sorted_acts:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected

# Time: O(n log n) — sorting plus O(n) DP pass with binary search
# Space: O(n) — DP table of size n
def weighted_activity_selection(activities):
    sorted_acts = sorted(activities, key=lambda a: a[1])
    n = len(sorted_acts)
    if n == 0:
        return 0
    finish_times = [a[1] for a in sorted_acts]

    def latest_compatible(i):
        lo, hi = 0, i - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if finish_times[mid] <= sorted_acts[i][0]:
                if mid + 1 <= i - 1 and finish_times[mid + 1] <= sorted_acts[i][0]:
                    lo = mid + 1
                else:
                    return mid
            else:
                hi = mid - 1
        return -1

    dp = [0] * n
    dp[0] = sorted_acts[0][2]
    for i in range(1, n):
        include = sorted_acts[i][2]
        p = latest_compatible(i)
        if p != -1:
            include += dp[p]
        dp[i] = max(dp[i - 1], include)
    return dp[n - 1]
