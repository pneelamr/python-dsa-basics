# Binary Tree: Hierarchical structure where each node has at most two children (left and right).
# Nodes are stored as dicts with 'val', 'left', and 'right' keys.
# Includes in-order, pre-order, post-order, and level-order traversals.

def create_node(value):
    return [value, None, None]  # [value, left, right]


# Time: O(h) where h=height — O(n) worst case (skewed), O(log n) balanced
# Space: O(h) — recursive call stack depth equals tree height
def insert(root, value):
    if root is None:
        return create_node(value)
    if value < root[0]:
        root[1] = insert(root[1], value)
    else:
        root[2] = insert(root[2], value)
    return root


def search(root, value):
    if root is None:
        return False
    if value == root[0]:
        return True
    if value < root[0]:
        return search(root[1], value)
    return search(root[2], value)


def inorder(root):
    if root is None:
        return []
    return inorder(root[1]) + [root[0]] + inorder(root[2])


def preorder(root):
    if root is None:
        return []
    return [root[0]] + preorder(root[1]) + preorder(root[2])


def postorder(root):
    if root is None:
        return []
    return postorder(root[1]) + postorder(root[2]) + [root[0]]


def display(root):
    print("inorder:", inorder(root))
