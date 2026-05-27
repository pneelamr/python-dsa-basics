# Prime Factorization: Decompose an integer into its prime factors using trial division up to sqrt(n).
# Divide out 2 first, then check odd divisors; any remaining factor > 1 is prime.
# Includes primality testing and listing all divisors of n.

# Time: O(sqrt(n)) — trial division up to sqrt(n)
# Space: O(log n) — at most log2(n) prime factors in the result list
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)
    return factors

# Time: O(sqrt(n)) — check divisibility up to sqrt(n)
# Space: O(1) — constant extra space
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

# Time: O(sqrt(n)) — find divisors up to sqrt(n) and mirror them
# Space: O(d(n)) — d(n) is the number of divisors of n
def all_divisors(n):
    small = []
    large = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d != n // d:
                large.append(n // d)
        d += 1
    return small + large[::-1]
