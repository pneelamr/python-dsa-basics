# Heap: Complete binary tree satisfying the heap property — parent ≤ children (min-heap).
# This implementation wraps Python's heapq module for push, pop, and peek.
# Common uses: priority queues, scheduling, heap sort.

import heapq


# Time: O(log n) — push/pop maintain heap property by sifting up/down
# Space: O(n) — stores n elements in the heap list
def push(heap, value):
    heapq.heappush(heap, value)


def pop(heap):
    if is_empty(heap):
        raise IndexError("pop from empty heap")
    return heapq.heappop(heap)


def peek(heap):
    if is_empty(heap):
        raise IndexError("peek from empty heap")
    return heap[0]


def is_empty(heap):
    return len(heap) == 0


def display(heap):
    print(heap)
