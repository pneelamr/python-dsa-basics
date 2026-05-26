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
