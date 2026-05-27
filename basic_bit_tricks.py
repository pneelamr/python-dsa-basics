# Bit Tricks: Common bitwise patterns for counting, detecting, and manipulating integer bit patterns.
# Brian Kernighan's algorithm counts set bits in O(k) where k is the number of set bits.
# XOR properties enable swapping without temp, finding unique elements, and detecting missing numbers.

# Time: O(k) — k is the number of set bits; each iteration clears one set bit
# Space: O(1) — constant extra space
def count_set_bits(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

# Time: O(1) — single AND comparison
# Space: O(1) — constant extra space
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Time: O(1) — three XOR operations, no extra variable
# Space: O(1) — constant extra space
def xor_swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Time: O(n) — single pass XOR over all elements
# Space: O(1) — constant extra space
def find_single(arr):
    result = 0
    for x in arr:
        result ^= x
    return result

# Time: O(n) — XOR all values 1..n then XOR with array elements
# Space: O(1) — constant extra space
def find_missing(arr, n):
    result = 0
    for i in range(1, n + 1):
        result ^= i
    for x in arr:
        result ^= x
    return result

# Time: O(bit_length) — iterate over half the bits to swap pairs
# Space: O(1) — constant extra space
def reverse_bits(n, bit_length):
    result = 0
    for _ in range(bit_length):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
