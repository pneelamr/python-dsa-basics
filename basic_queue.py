# Queue: FIFO (First-In, First-Out) data structure backed by a plain Python list.
# Elements are enqueued at the back and dequeued from the front.
# Common uses: task scheduling, BFS, buffering.

# Time: O(1) enqueue (append), O(n) dequeue (pop(0) shifts all elements)
# Space: O(n) — stores up to n elements
def enqueue(queue, value):
    queue.append(value)


def dequeue(queue):
    if is_empty(queue):
        raise IndexError("dequeue from empty queue")
    return queue.pop(0)


def peek(queue):
    if is_empty(queue):
        raise IndexError("peek from empty queue")
    return queue[0]


def is_empty(queue):
    return len(queue) == 0


def display(queue):
    print(queue)
