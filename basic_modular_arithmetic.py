# Modular Arithmetic: Arithmetic operations on residues modulo m, fundamental in cryptography and number theory.
# Modular exponentiation computes base^exp mod m in O(log exp) using repeated squaring.
# Modular inverse finds x such that a*x ≡ 1 (mod m) using Fermat's little theorem (prime m) or extended GCD.

# Time: O(log exp) — repeated squaring halves the exponent each iteration
# Space: O(1) — iterative, constant extra space
def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Time: O(log mod) — one call to mod_pow with exponent mod-2
# Space: O(1) — constant extra space
def mod_inverse_fermat(a, mod):
    return mod_pow(a, mod - 2, mod)

# Time: O(log(min(a, mod))) — extended Euclidean algorithm
# Space: O(1) — iterative, constant extra space
def mod_inverse_extended_gcd(a, mod):
    g, x, _ = _extended_gcd(a, mod)
    if g != 1:
        return None
    return x % mod

def _extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = _extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

# Time: O(n log M) — n iterations each doing mod_inverse and mod_pow; M is product of moduli
# Space: O(1) — constant extra space beyond inputs
def chinese_remainder(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        inv = mod_inverse_extended_gcd(Mi, m)
        x = (x + r * Mi * inv) % M
    return x
