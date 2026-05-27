# Shell Sort: Generalization of insertion sort that sorts elements far apart first, then reduces the gap.
# Uses a gap sequence (here: gap = n//2, halved each pass) to move elements closer to their final position faster.
# Faster than O(n²) in practice; exact complexity depends on the gap sequence chosen.

# Time: O(n log n) average depending on gap sequence, O(n²) worst case
# Space: O(1) — sorts in-place using only gap and key variables
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2
