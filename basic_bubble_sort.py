# Bubble Sort: Simple comparison sort that repeatedly steps through the list swapping adjacent out-of-order pairs.
# Each full pass bubbles the current largest unsorted element to its final position.
# O(n²) time; includes an early-exit optimization when no swaps occur in a pass.

# Time: O(n²) worst/average, O(n) best (already sorted with early exit)
# Space: O(1) — sorts in-place with only a swap variable
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
