# Merge Sort: Divide-and-conquer sort that splits the array in half, recursively sorts each half, then merges.
# Merge step combines two sorted halves by comparing elements one at a time.
# Stable sort with guaranteed O(n log n) time; requires O(n) extra space.

# Time: O(n log n) — divides array into halves and merges in linear time each level
# Space: O(n) — merge creates temporary arrays totaling n elements
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
