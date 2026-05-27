# Linear Search: Simplest search algorithm that scans every element from start to end.
# Works on unsorted data and returns the first index where the target is found.
# O(n) time; useful when the array is small or unsorted.

# Time: O(n) — scans each element until target found or end reached
# Space: O(1) — only uses a loop index variable
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    return [i for i, val in enumerate(arr) if val == target]
