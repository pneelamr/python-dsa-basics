# Time: O(N! * N) — N! permutations, each takes O(N) to build
# Space: O(N) — recursion stack depth

def permutations(arr):
    result = []
    _generate(arr[:], 0, result)
    return result


def _generate(arr, start, result):
    if start == len(arr):
        result.append(arr[:])
        return
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        _generate(arr, start + 1, result)
        arr[start], arr[i] = arr[i], arr[start]


def permutations_with_duplicates(arr):
    arr.sort()
    result = []
    _generate_unique(arr, 0, result)
    return result


def _generate_unique(arr, start, result):
    if start == len(arr):
        result.append(arr[:])
        return
    seen = set()
    for i in range(start, len(arr)):
        if arr[i] in seen:
            continue
        seen.add(arr[i])
        arr[start], arr[i] = arr[i], arr[start]
        _generate_unique(arr, start + 1, result)
        arr[start], arr[i] = arr[i], arr[start]
