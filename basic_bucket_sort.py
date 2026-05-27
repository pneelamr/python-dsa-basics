# Time: O(n+k) average (uniform distribution), O(n²) worst (all elements in one bucket)
# Space: O(n+k) — n elements spread across k buckets
def bucket_sort(arr, num_buckets=10):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val

    buckets = [[] for _ in range(num_buckets)]

    for val in arr:
        if range_val == 0:
            index = 0
        else:
            index = int((val - min_val) / range_val * (num_buckets - 1))
        buckets[index].append(val)

    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result
