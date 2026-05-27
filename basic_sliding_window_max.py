# Sliding Window Maximum: Find the maximum value in every contiguous window of size k using a monotonic deque.
# Maintain a deque of indices in decreasing order of their values; the front always holds the current window max.
# Indices outside the window are popped from the front; smaller elements are popped from the back. O(n) time.

from collections import deque

# Time: O(n) — each index is pushed and popped from the deque at most once
# Space: O(k) — deque holds at most k indices at any time; output list is O(n-k+1)
def sliding_window_max(arr, k):
    if not arr or k <= 0:
        return []
    dq = deque()
    result = []
    for i, val in enumerate(arr):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] < val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

# Time: O(n) — each index is pushed and popped from the deque at most once
# Space: O(k) — deque holds at most k indices; output list is O(n-k+1)
def sliding_window_min(arr, k):
    if not arr or k <= 0:
        return []
    dq = deque()
    result = []
    for i, val in enumerate(arr):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[dq[-1]] > val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result
