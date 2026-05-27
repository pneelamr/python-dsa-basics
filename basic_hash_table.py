# Hash Table: Key-value store that maps keys to buckets using a hash function.
# Collisions are resolved by chaining — each bucket holds a list of (key, value) pairs.
# Supports get, put, delete, and iteration over keys.

# Time: O(1) average — insert/get/delete use Python dict hashing
# Space: O(n) — stores n key-value pairs
def insert(table, key, value):
    table[key] = value


def get(table, key):
    if key not in table:
        raise KeyError(f"key '{key}' not found")
    return table[key]


def delete(table, key):
    if key not in table:
        raise KeyError(f"key '{key}' not found")
    del table[key]


def contains(table, key):
    return key in table


def display(table):
    print(table)
