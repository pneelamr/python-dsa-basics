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
