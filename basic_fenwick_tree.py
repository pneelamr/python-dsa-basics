def create(arr):
    n = len(arr)
    tree = [0] * (n + 1)  # 1-indexed
    ft = {'tree': tree, 'n': n}
    for i, val in enumerate(arr):
        update(ft, i + 1, val)
    return ft


# Time: O(log n) — update/prefix_sum traverse at most log n nodes via bit tricks
# Space: O(n) — tree array of size n+1
def update(ft, index, delta):
    while index <= ft['n']:
        ft['tree'][index] += delta
        index += index & (-index)  # move to next responsible node


def prefix_sum(ft, index):
    total = 0
    while index > 0:
        total += ft['tree'][index]
        index -= index & (-index)  # move to parent
    return total


def range_query(ft, l, r):
    return prefix_sum(ft, r) - prefix_sum(ft, l - 1)


def point_update(ft, index, old_val, new_val):
    update(ft, index, new_val - old_val)


def display(ft):
    print(f"prefix sums:")
    for i in range(1, ft['n'] + 1):
        print(f"  prefix_sum(1,{i}) = {prefix_sum(ft, i)}")
