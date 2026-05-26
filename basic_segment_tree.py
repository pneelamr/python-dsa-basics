def create(arr):
    n = len(arr)
    tree = [0] * (4 * n)
    _build(arr, tree, 0, n - 1, 0)
    return {'tree': tree, 'arr': arr[:], 'n': n}


def _build(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
        return
    mid = (start + end) // 2
    _build(arr, tree, start, mid, 2 * node + 1)
    _build(arr, tree, mid + 1, end, 2 * node + 2)
    tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def query(st, l, r):
    return _query(st['tree'], 0, st['n'] - 1, l, r, 0)


def _query(tree, start, end, l, r, node):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    return (_query(tree, start, mid, l, r, 2 * node + 1) +
            _query(tree, mid + 1, end, l, r, 2 * node + 2))


def update(st, index, value):
    diff = value - st['arr'][index]
    st['arr'][index] = value
    _update(st['tree'], 0, st['n'] - 1, index, diff, 0)


def _update(tree, start, end, index, diff, node):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        _update(tree, start, mid, index, diff, 2 * node + 1)
        _update(tree, mid + 1, end, index, diff, 2 * node + 2)


def display(st):
    print(f"array: {st['arr']}")
    print(f"range sums:")
    for i in range(st['n']):
        for j in range(i, st['n']):
            print(f"  sum({i},{j}) = {query(st, i, j)}")
