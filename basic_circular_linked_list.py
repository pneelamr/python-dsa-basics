# Circular Linked List: Singly linked list where the tail node's next pointer wraps back to the head.
# Useful for round-robin scheduling and cyclic iteration without a null terminator.
# Traversal must track the starting node to detect when the cycle completes.

def create_list():
    return {'head': None}


def create_node(value):
    return {'val': value, 'next': None}


# Time: O(n) insert_front/insert_back/delete/search — must traverse to find tail or target
# Space: O(n) — n nodes stored in the circular list
def insert_front(ll, value):
    node = create_node(value)
    if ll['head'] is None:
        node['next'] = node
        ll['head'] = node
        return
    tail = _get_tail(ll)
    node['next'] = ll['head']
    tail['next'] = node
    ll['head'] = node


def insert_back(ll, value):
    node = create_node(value)
    if ll['head'] is None:
        node['next'] = node
        ll['head'] = node
        return
    tail = _get_tail(ll)
    tail['next'] = node
    node['next'] = ll['head']


def delete(ll, value):
    if ll['head'] is None:
        return False
    if ll['head']['val'] == value:
        if ll['head']['next'] == ll['head']:
            ll['head'] = None
        else:
            tail = _get_tail(ll)
            ll['head'] = ll['head']['next']
            tail['next'] = ll['head']
        return True
    current = ll['head']
    while current['next'] != ll['head']:
        if current['next']['val'] == value:
            current['next'] = current['next']['next']
            return True
        current = current['next']
    return False


def search(ll, value):
    if ll['head'] is None:
        return -1
    current = ll['head']
    index = 0
    while True:
        if current['val'] == value:
            return index
        current = current['next']
        index += 1
        if current == ll['head']:
            break
    return -1


def display(ll):
    if ll['head'] is None:
        print('None')
        return
    result = []
    current = ll['head']
    while True:
        result.append(str(current['val']))
        current = current['next']
        if current == ll['head']:
            break
    print(' -> '.join(result) + ' -> (back to head)')


def _get_tail(ll):
    current = ll['head']
    while current['next'] != ll['head']:
        current = current['next']
    return current
