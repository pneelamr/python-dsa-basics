def push_front(deque, value):
    deque.insert(0, value)


def push_back(deque, value):
    deque.append(value)


def pop_front(deque):
    if is_empty(deque):
        raise IndexError("pop from empty deque")
    return deque.pop(0)


def pop_back(deque):
    if is_empty(deque):
        raise IndexError("pop from empty deque")
    return deque.pop()


def peek_front(deque):
    if is_empty(deque):
        raise IndexError("peek from empty deque")
    return deque[0]


def peek_back(deque):
    if is_empty(deque):
        raise IndexError("peek from empty deque")
    return deque[-1]


def is_empty(deque):
    return len(deque) == 0


def display(deque):
    print(deque)
