# Time: O(n+k) where k=value range — counts n elements then iterates over k buckets
# Space: O(k) — count array proportional to value range k
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    offset = min_val
    count = [0] * (max_val - min_val + 1)

    for val in arr:
        count[val - offset] += 1

    result = []
    for i, freq in enumerate(count):
        result.extend([i + offset] * freq)

    return result
