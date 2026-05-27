# AVL Tree: Self-balancing binary search tree maintaining a balance factor of -1, 0, or +1 at every node.
# After each insert or delete, rotations (LL, RR, LR, RL) restore balance.
# Guarantees O(log n) search, insert, and delete even in worst-case scenarios.

def create_node(value):
    return {'val': value, 'left': None, 'right': None, 'height': 1}


def get_height(node):
    return node['height'] if node else 0


def get_balance(node):
    return get_height(node['left']) - get_height(node['right']) if node else 0


def update_height(node):
    node['height'] = 1 + max(get_height(node['left']), get_height(node['right']))


def rotate_right(z):
    y = z['left']
    t = y['right']
    y['right'] = z
    z['left'] = t
    update_height(z)
    update_height(y)
    return y


def rotate_left(z):
    y = z['right']
    t = y['left']
    y['left'] = z
    z['right'] = t
    update_height(z)
    update_height(y)
    return y


# Time: O(log n) — AVL balance property guarantees height is O(log n)
# Space: O(log n) — recursive call stack bounded by tree height
def insert(root, value):
    if root is None:
        return create_node(value)
    if value < root['val']:
        root['left'] = insert(root['left'], value)
    elif value > root['val']:
        root['right'] = insert(root['right'], value)
    else:
        return root  # duplicates not allowed

    update_height(root)
    balance = get_balance(root)

    # Left-Left
    if balance > 1 and value < root['left']['val']:
        return rotate_right(root)
    # Right-Right
    if balance < -1 and value > root['right']['val']:
        return rotate_left(root)
    # Left-Right
    if balance > 1 and value > root['left']['val']:
        root['left'] = rotate_left(root['left'])
        return rotate_right(root)
    # Right-Left
    if balance < -1 and value < root['right']['val']:
        root['right'] = rotate_right(root['right'])
        return rotate_left(root)

    return root


def search(root, value):
    if root is None:
        return False
    if value == root['val']:
        return True
    if value < root['val']:
        return search(root['left'], value)
    return search(root['right'], value)


def inorder(root):
    if root is None:
        return []
    return inorder(root['left']) + [root['val']] + inorder(root['right'])


def display(root, level=0, prefix='Root: '):
    if root is None:
        return
    print(' ' * (level * 4) + prefix + str(root['val']) + f' (h={root["height"]})')
    if root['left'] or root['right']:
        if root['left']:
            display(root['left'], level + 1, 'L: ')
        if root['right']:
            display(root['right'], level + 1, 'R: ')
