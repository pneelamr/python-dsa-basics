# Time: O(C(N,K) * K) — C(N,K) combinations, each takes O(K) to build
# Space: O(K) — recursion stack depth

def combinations(arr, k):
    result = []
    _generate(arr, k, 0, [], result)
    return result


def _generate(arr, k, start, current, result):
    if len(current) == k:
        result.append(current[:])
        return
    for i in range(start, len(arr)):
        current.append(arr[i])
        _generate(arr, k, i + 1, current, result)
        current.pop()


def combinations_sum(arr, target):
    result = []
    arr.sort()
    _generate_sum(arr, target, 0, [], result)
    return result


def _generate_sum(arr, target, start, current, result):
    if target == 0:
        result.append(current[:])
        return
    for i in range(start, len(arr)):
        if arr[i] > target:
            break
        current.append(arr[i])
        _generate_sum(arr, target - arr[i], i + 1, current, result)
        current.pop()
