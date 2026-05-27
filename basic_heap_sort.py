# Heap Sort: Comparison-based sort that first builds a max-heap in-place, then sorts.
# Repeatedly swaps the root (max) with the last element and sifts down to restore the heap.
# In-place with no extra memory; always O(n log n) unlike quicksort.

# Time: O(n log n) — build heap O(n), then extract each of n elements in O(log n)
# Space: O(1) — sorts in-place using heap operations on the input array
def heap_sort(arr):
    n = len(arr)

    # build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(arr, n, i)

    # extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # move current root (max) to end
        _sift_down(arr, i, 0)


def _sift_down(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _sift_down(arr, n, largest)
