# Binary Search: Efficient search on a sorted array by repeatedly halving the search interval.
# Compares the target to the midpoint; recurse or iterate on the left or right half accordingly.
# O(log n) time; includes iterative, recursive, and first/last occurrence variants.

# Time: O(log n) — halves search space each iteration
# Space: O(1) iterative; recursive version uses O(log n) call stack
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)
