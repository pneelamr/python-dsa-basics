# Binary Exponentiation: Compute base^exp in O(log exp) using repeated squaring (divide and conquer).
# At each step, square the base and halve the exponent; if exponent is odd, multiply result by base once more.
# The modular variant keeps numbers bounded and is essential in cryptography and competitive programming.

# Time: O(log exp) — exponent is halved at each iteration, giving log2(exp) steps
# Space: O(1) — iterative; only a few scalar variables
def fast_power(base, exp):
    if exp < 0:
        return fast_power(1, -exp)
    result = 1
    b = base
    e = exp
    while e > 0:
        if e % 2 == 1:
            result *= b
        b *= b
        e //= 2
    return result

# Time: O(log exp) — same halving loop as fast_power with a modulo at each step
# Space: O(1) — iterative with constant extra variables
def fast_power_mod(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    b = base % mod
    e = exp
    while e > 0:
        if e % 2 == 1:
            result = (result * b) % mod
        b = (b * b) % mod
        e //= 2
    return result

def _mat_mul(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0],
         A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0],
         A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

# Time: O(log n) — matrix is squared O(log n) times; each 2×2 multiply is O(1)
# Space: O(log n) — recursion stack depth is O(log n)
def matrix_power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    if n == 1:
        return [row[:] for row in matrix]
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2)
        return _mat_mul(half, half)
    else:
        return _mat_mul(matrix, matrix_power(matrix, n - 1))
