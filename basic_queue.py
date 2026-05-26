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
