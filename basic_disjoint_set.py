def create(n):
    return {'parent': list(range(n)), 'rank': [0] * n}


def find(ds, x):
    if ds['parent'][x] != x:
        ds['parent'][x] = find(ds, ds['parent'][x])  # path compression
    return ds['parent'][x]


def union(ds, x, y):
    root_x = find(ds, x)
    root_y = find(ds, y)
    if root_x == root_y:
        return

    # union by rank — attach smaller tree under larger tree
    if ds['rank'][root_x] < ds['rank'][root_y]:
        ds['parent'][root_x] = root_y
    elif ds['rank'][root_x] > ds['rank'][root_y]:
        ds['parent'][root_y] = root_x
    else:
        ds['parent'][root_y] = root_x
        ds['rank'][root_x] += 1


def connected(ds, x, y):
    return find(ds, x) == find(ds, y)


def display(ds):
    groups = {}
    for i in range(len(ds['parent'])):
        root = find(ds, i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    for root, members in groups.items():
        print(f"  group {root}: {members}")
