# Heap (Array): Min-heap built from scratch on a plain Python list without heapq.
# Parent-child relationships are encoded by index: parent at i, children at 2i+1 and 2i+2.
# Supports insert (sift-up) and extract-min (sift-down), both O(log n).

def create():
    return []


# Time: O(log n) — push/pop sift up/down through at most log n levels
# Space: O(n) — heap stored as a plain list of n elements
def push(heap, value):
    heap.append(value)
    _sift_up(heap, len(heap) - 1)


def pop(heap):
    if is_empty(heap):
        raise IndexError("pop from empty heap")
    _swap(heap, 0, len(heap) - 1)
    value = heap.pop()
    _sift_down(heap, 0)
    return value


def peek(heap):
    if is_empty(heap):
        raise IndexError("peek from empty heap")
    return heap[0]


def is_empty(heap):
    return len(heap) == 0


def _parent(i):
    return (i - 1) // 2


def _left(i):
    return 2 * i + 1


def _right(i):
    return 2 * i + 2


def _swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def _sift_up(heap, i):
    while i > 0 and heap[i] < heap[_parent(i)]:
        _swap(heap, i, _parent(i))
        i = _parent(i)


def _sift_down(heap, i):
    n = len(heap)
    smallest = i
    left = _left(i)
    right = _right(i)
    if left < n and heap[left] < heap[smallest]:
        smallest = left
    if right < n and heap[right] < heap[smallest]:
        smallest = right
    if smallest != i:
        _swap(heap, i, smallest)
        _sift_down(heap, smallest)


def display(heap):
    print(heap)
