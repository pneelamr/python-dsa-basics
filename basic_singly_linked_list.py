def create_list():
    return {'head': None}


def create_node(value):
    return {'val': value, 'next': None}


def insert_front(ll, value):
    node = create_node(value)
    node['next'] = ll['head']
    ll['head'] = node


def insert_back(ll, value):
    node = create_node(value)
    if ll['head'] is None:
        ll['head'] = node
        return
    current = ll['head']
    while current['next']:
        current = current['next']
    current['next'] = node


def delete(ll, value):
    if ll['head'] is None:
        return False
    if ll['head']['val'] == value:
        ll['head'] = ll['head']['next']
        return True
    current = ll['head']
    while current['next']:
        if current['next']['val'] == value:
            current['next'] = current['next']['next']
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
    print(' -> '.join(result) + ' -> None')
