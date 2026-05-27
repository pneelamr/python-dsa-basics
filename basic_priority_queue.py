import heapq


# Time: O(log n) — enqueue/dequeue maintain heap order by sifting up/down
# Space: O(n) — stores n (priority, value) pairs in the heap
def enqueue(pq, value, priority):
    heapq.heappush(pq, (priority, value))


def dequeue(pq):
    if is_empty(pq):
        raise IndexError("dequeue from empty priority queue")
    priority, value = heapq.heappop(pq)
    return value, priority


def peek(pq):
    if is_empty(pq):
        raise IndexError("peek from empty priority queue")
    priority, value = pq[0]
    return value, priority


def is_empty(pq):
    return len(pq) == 0


def display(pq):
    for priority, value in sorted(pq):
        print(f"  priority {priority}: {value}")
