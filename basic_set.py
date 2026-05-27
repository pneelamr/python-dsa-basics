# Set: Unordered collection of unique elements backed by Python's built-in set type.
# Supports add, remove, membership testing, and set operations (union, intersection, difference).
# All core operations run in O(1) average due to the underlying hash table.

# Time: O(1) average — add/remove/contains use Python set hashing
# Space: O(n) — stores n elements
def add(s, value):
    s.add(value)


def remove(s, value):
    if value not in s:
        raise KeyError(f"'{value}' not found in set")
    s.remove(value)


def contains(s, value):
    return value in s


def union(s1, s2):
    return s1 | s2


def intersection(s1, s2):
    return s1 & s2


def difference(s1, s2):
    return s1 - s2


def display(s):
    print(s)
