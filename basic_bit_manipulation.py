# Bit Manipulation: Direct operations on individual bits of an integer using bitwise operators.
# get, set, clear, and toggle a bit at position i; find the lowest set bit; check sign and parity.
# Bit operations are O(1) and often replace conditionals and arithmetic for performance-critical code.

# Time: O(1) — single bitwise shift and AND
# Space: O(1) — constant extra space
def get_bit(n, i):
    return (n >> i) & 1

# Time: O(1) — single bitwise shift and OR
# Space: O(1) — constant extra space
def set_bit(n, i):
    return n | (1 << i)

# Time: O(1) — single bitwise shift, NOT, and AND
# Space: O(1) — constant extra space
def clear_bit(n, i):
    return n & ~(1 << i)

# Time: O(1) — single bitwise shift and XOR
# Space: O(1) — constant extra space
def toggle_bit(n, i):
    return n ^ (1 << i)

# Time: O(1) — clear then set depending on value v
# Space: O(1) — constant extra space
def update_bit(n, i, v):
    n = clear_bit(n, i)
    return n | (v << i)

# Time: O(1) — single AND with 1
# Space: O(1) — constant extra space
def is_odd(n):
    return (n & 1) == 1

# Time: O(1) — isolate lowest set bit using two's complement identity n & (-n)
# Space: O(1) — constant extra space
def lowest_set_bit(n):
    return n & (-n)

# Time: O(1) — clear lowest set bit using n & (n-1)
# Space: O(1) — constant extra space
def clear_lowest_set_bit(n):
    return n & (n - 1)
