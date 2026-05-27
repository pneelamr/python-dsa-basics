# Karatsuba Multiplication: Divide-and-conquer integer multiplication reducing recursive calls from 4 to 3.
# Split each n-digit number into two halves (high and low); compute ac, bd, and (a+b)(c+d)-ac-bd instead of all four products.
# O(n^1.585) time vs grade-school O(n²); the constant factor makes it practical only for large integers.

# Time: O(n^1.585) — three recursive calls on n/2-digit numbers; exponent log2(3) ≈ 1.585
# Space: O(n log n) — recursion depth O(log n), each level holds O(n)-bit intermediates
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    m = 10 ** half
    a, b = divmod(x, m)
    c, d = divmod(y, m)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * (m * m) + ad_bc * m + bd
