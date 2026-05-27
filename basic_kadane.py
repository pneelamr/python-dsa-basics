# Kadane's Algorithm: Linear-time algorithm finding the maximum sum contiguous subarray.
# Track a running current_sum; reset to 0 (or current element) when it goes negative.
# The circular variant considers both the normal max and the total_sum minus the minimum subarray.

# Time: O(n) — single linear pass through the array
# Space: O(1) — only scalar variables for current and global max
def max_subarray(arr):
    if not arr:
        return 0
    max_sum = arr[0]
    current = arr[0]
    for num in arr[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum

# Time: O(n) — single pass; tracks start/end indices alongside the running sum
# Space: O(1) — constant extra variables
def max_subarray_with_indices(arr):
    if not arr:
        return (0, -1, -1)
    max_sum = arr[0]
    current = arr[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(1, len(arr)):
        if arr[i] > current + arr[i]:
            current = arr[i]
            temp_start = i
        else:
            current = current + arr[i]
        if current > max_sum:
            max_sum = current
            start = temp_start
            end = i
    return (max_sum, start, end)

# Time: O(n) — two Kadane passes (max subarray + min subarray) plus a total sum scan
# Space: O(1) — constant extra space
def max_circular_subarray(arr):
    if not arr:
        return 0
    max_normal = max_subarray(arr)
    total = sum(arr)
    negated = [-x for x in arr]
    min_subarray_sum = -max_subarray(negated)
    if total == min_subarray_sum:
        return max_normal
    max_circular = total - min_subarray_sum
    return max(max_normal, max_circular)
