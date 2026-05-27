# Subsets (Power Set): Enumerate all 2ⁿ subsets of a set of n elements, including the empty set.
# Backtracking builds each subset by choosing to include or exclude each element in turn.
# Iterative variant uses bit masking: each integer from 0 to 2ⁿ-1 represents one subset.

# Time: O(2^N) — 2 choices per element (include or exclude), N elements
# Space: O(N) — recursion stack depth

def subsets(arr):
    result = []
    _generate(arr, 0, [], result)
    return result


def _generate(arr, index, current, result):
    result.append(current[:])
    for i in range(index, len(arr)):
        current.append(arr[i])
        _generate(arr, i + 1, current, result)
        current.pop()


def subsets_iterative(arr):
    result = [[]]
    for val in arr:
        result += [subset + [val] for subset in result]
    return result


def subsets_with_duplicates(arr):
    arr.sort()
    result = []
    _generate_unique(arr, 0, [], result)
    return result


def _generate_unique(arr, index, current, result):
    result.append(current[:])
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i - 1]:
            continue
        current.append(arr[i])
        _generate_unique(arr, i + 1, current, result)
        current.pop()
