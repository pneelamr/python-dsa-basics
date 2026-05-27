# Insertion Sort: Builds the sorted array one element at a time by inserting each new element into its correct position.
# Efficient for small arrays and nearly sorted data; stable and in-place.
# O(n²) worst case; O(n) best case (already sorted).

# Time: O(n²) worst/average, O(n) best (already sorted)
# Space: O(1) — sorts in-place using only a key variable
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
