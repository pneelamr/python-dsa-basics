from collections import deque


def create(capacity):
    return {'cache': {}, 'order': deque(), 'capacity': capacity}


# Time: O(n) — get/put call deque.remove which scans up to n elements
# Space: O(capacity) — cache and order deque bounded by capacity
def get(lru, key):
    if key not in lru['cache']:
        return -1
    lru['order'].remove(key)
    lru['order'].append(key)
    return lru['cache'][key]


def put(lru, key, value):
    if key in lru['cache']:
        lru['order'].remove(key)
    elif len(lru['cache']) == lru['capacity']:
        oldest = lru['order'].popleft()
        del lru['cache'][oldest]
    lru['cache'][key] = value
    lru['order'].append(key)


def display(lru):
    ordered = [(k, lru['cache'][k]) for k in lru['order']]
    print(f"cache (LRU→MRU): {ordered} (capacity={lru['capacity']})")
