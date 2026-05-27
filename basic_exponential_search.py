# Time: O(log n) — exponential range-finding then binary search, both O(log n)
# Space: O(1) — iterative with only index variables
def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return _binary_search(arr, target, i // 2, min(i, n - 1))


def _binary_search(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
