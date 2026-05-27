# Sliding Window (Fixed): Maintain a window of exactly k elements, sliding one step at a time over an array.
# Add the incoming element and subtract the outgoing element each step — avoids recomputing the window sum.
# O(n) time by processing each element exactly twice (once added, once removed).

# Time: O(n) — single pass; initial window built in O(k), then n-k slides each O(1)
# Space: O(1) — only scalar variables tracking the window sum
def max_sum_subarray(arr, k):
    if not arr or k > len(arr):
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Time: O(n) — single pass; same sliding approach as max_sum_subarray
# Space: O(1) — only scalar variables
def min_sum_subarray(arr, k):
    if not arr or k > len(arr):
        return None
    window_sum = sum(arr[:k])
    min_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        min_sum = min(min_sum, window_sum)
    return min_sum

# Time: O(n) — single pass over n elements computing each window sum in O(1)
# Space: O(1) — only the count and running sum are stored
def count_subarrays_with_sum(arr, k, target):
    if not arr or k > len(arr):
        return 0
    window_sum = sum(arr[:k])
    count = 1 if window_sum == target else 0
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum == target:
            count += 1
    return count
