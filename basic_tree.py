def create_node(value):
    return {'val': value, 'children': []}


# Time: O(1) add_child, O(n) search/bfs/dfs — visits all n nodes
# Space: O(n) — n nodes stored in the tree
def add_child(parent, value):
    child = create_node(value)
    parent['children'].append(child)
    return child


def search(root, value):
    if root['val'] == value:
        return root
    for child in root['children']:
        result = search(child, value)
        if result:
            return result
    return None


def bfs(root):
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node['val'])
        for child in node['children']:
            queue.append(child)
    return result


def dfs(root):
    result = [root['val']]
    for child in root['children']:
        result += dfs(child)
    return result


def display(root, level=0):
    print('  ' * level + str(root['val']))
    for child in root['children']:
        display(child, level + 1)
