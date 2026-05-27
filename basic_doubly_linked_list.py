# Doubly Linked List: Linked list where each node holds pointers to both the next and previous nodes.
# Enables O(1) insertion and deletion at both ends (head and tail).
# Useful as the backbone of LRU caches and deques.

def create_list():
    return {'head': None, 'tail': None}


def create_node(value):
    return {'val': value, 'prev': None, 'next': None}


# Time: O(1) insert_front/insert_back, O(n) delete/search — traverses up to n nodes
# Space: O(n) — n nodes stored with prev/next pointers
def insert_front(ll, value):
    node = create_node(value)
    if ll['head'] is None:
        ll['head'] = ll['tail'] = node
        return
    node['next'] = ll['head']
    ll['head']['prev'] = node
    ll['head'] = node


def insert_back(ll, value):
    node = create_node(value)
    if ll['tail'] is None:
        ll['head'] = ll['tail'] = node
        return
    node['prev'] = ll['tail']
    ll['tail']['next'] = node
    ll['tail'] = node


def delete(ll, value):
    current = ll['head']
    while current:
        if current['val'] == value:
            if current['prev']:
                current['prev']['next'] = current['next']
            else:
                ll['head'] = current['next']
            if current['next']:
                current['next']['prev'] = current['prev']
            else:
                ll['tail'] = current['prev']
            return True
        current = current['next']
    return False


def search(ll, value):
    current = ll['head']
    index = 0
    while current:
        if current['val'] == value:
            return index
        current = current['next']
        index += 1
    return -1


def display(ll):
    result = []
    current = ll['head']
    while current:
        result.append(str(current['val']))
        current = current['next']
    print('None <-> ' + ' <-> '.join(result) + ' <-> None')


def display_reverse(ll):
    result = []
    current = ll['tail']
    while current:
        result.append(str(current['val']))
        current = current['prev']
    print('None <-> ' + ' <-> '.join(result) + ' <-> None')
