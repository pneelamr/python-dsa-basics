# Jump Search: Searches a sorted array by jumping ahead in fixed steps of size √n.
# Once the block containing the target is identified, a linear scan within that block finds it.
# O(√n) time — sits between linear O(n) and binary O(log n) search in complexity.

import math


# Time: O(√n) — jumps forward √n steps then does linear scan of at most √n elements
# Space: O(1) — only uses index variables
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1
