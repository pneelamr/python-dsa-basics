# Selection Sort: Divides the array into sorted and unsorted regions, repeatedly finding the minimum of the unsorted region.
# Swaps the found minimum into the next position of the sorted region.
# Always O(n²) comparisons regardless of input order; not stable but in-place.

# Time: O(n²) all cases — always scans remaining unsorted portion
# Space: O(1) — sorts in-place with no extra allocations
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
