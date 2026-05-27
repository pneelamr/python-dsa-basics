# Time: O(log log n) average (uniform data), O(n) worst (skewed distribution)
# Space: O(1) — only uses index and position variables
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1
