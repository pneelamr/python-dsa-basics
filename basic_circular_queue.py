# Circular Queue: Fixed-capacity queue using a list with wrap-around head and tail pointers.
# Reuses freed slots at the front when new elements are enqueued, avoiding shifting.
# Enqueue and dequeue are both O(1); capacity is set at creation time.

def create_queue(capacity):
    return {'data': [None] * capacity, 'front': 0, 'rear': 0, 'size': 0, 'capacity': capacity}


# Time: O(1) — enqueue/dequeue use modular index arithmetic with no shifting
# Space: O(n) — fixed-capacity array of n slots
def enqueue(cq, value):
    if is_full(cq):
        raise OverflowError("circular queue is full")
    cq['data'][cq['rear']] = value
    cq['rear'] = (cq['rear'] + 1) % cq['capacity']
    cq['size'] += 1


def dequeue(cq):
    if is_empty(cq):
        raise IndexError("dequeue from empty circular queue")
    value = cq['data'][cq['front']]
    cq['data'][cq['front']] = None
    cq['front'] = (cq['front'] + 1) % cq['capacity']
    cq['size'] -= 1
    return value


def peek(cq):
    if is_empty(cq):
        raise IndexError("peek from empty circular queue")
    return cq['data'][cq['front']]


def is_empty(cq):
    return cq['size'] == 0


def is_full(cq):
    return cq['size'] == cq['capacity']


def display(cq):
    result = []
    for i in range(cq['size']):
        index = (cq['front'] + i) % cq['capacity']
        result.append(str(cq['data'][index]))
    print('[' + ', '.join(result) + f'] (size={cq["size"]}, capacity={cq["capacity"]})')
