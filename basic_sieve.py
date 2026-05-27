# Sieve of Eratosthenes: Finds all prime numbers up to n in O(n log log n) time.
# Mark all multiples of each prime starting from 2 as composite; unmarked numbers are prime.
# Segmented sieve extends this to arbitrary ranges [low, high] using O(sqrt(high)) space.

import math

# Time: O(n log log n) — each prime p marks n/p multiples; sum over primes is n log log n
# Space: O(n) — boolean array of size n+1
def sieve(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

# Time: O((high - low + 1) log log high + sqrt(high) log log sqrt(high)) — sieve small primes then mark range
# Space: O(sqrt(high) + high - low + 1) — small primes list and range boolean array
def segmented_sieve(low, high):
    if high < 2:
        return []
    limit = int(math.isqrt(high)) + 1
    small_primes = sieve(limit)
    size = high - low + 1
    is_prime_range = [True] * size
    if low == 0:
        is_prime_range[0] = False
    if low <= 1 <= high:
        is_prime_range[1 - low] = False
    for p in small_primes:
        start = max(p * p, ((low + p - 1) // p) * p)
        if start == p:
            start += p
        for j in range(start, high + 1, p):
            is_prime_range[j - low] = False
    return [low + i for i in range(size) if is_prime_range[i]]

# Time: O(sqrt(n)) — trial division up to the square root of n
# Space: O(1) — only loop counter and remainder operations
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
