# String Hashing: Polynomial rolling hash enabling O(1) substring equality checks after O(n) preprocessing.
# Hash of s[l..r] = (s[l]*b^(r-l) + ... + s[r]) mod m, computed from prefix hashes in constant time.
# Double hashing (two different bases/moduli) reduces collision probability to near zero.

# Time: O(n) — single pass to compute prefix hashes and powers of base
# Space: O(n) — two arrays of length n+1 for prefix_hash and pow_base
def build_hash(s, base=131, mod=10**9+7):
    n = len(s)
    prefix_hash = [0] * (n + 1)
    pow_base = [1] * (n + 1)
    for i in range(n):
        prefix_hash[i + 1] = (prefix_hash[i] * base + ord(s[i])) % mod
        pow_base[i + 1] = (pow_base[i] * base) % mod
    return prefix_hash, pow_base

# Time: O(1) — arithmetic on precomputed prefix hash values
# Space: O(1) — constant extra space
def get_hash(prefix_hash, pow_base, l, r, mod=10**9+7):
    return (prefix_hash[r + 1] - prefix_hash[l] * pow_base[r - l + 1]) % mod

# Time: O(1) — two calls to get_hash each O(1)
# Space: O(1) — constant extra space
def are_equal(ph1, pb1, l1, r1, ph2, pb2, l2, r2, mod=10**9+7):
    return get_hash(ph1, pb1, l1, r1, mod) == get_hash(ph2, pb2, l2, r2, mod)

# Time: O(n) — sliding window hashing over all substrings of given length
# Space: O(n) — hash set for seen hashes and result list
def find_duplicate_substrings(s, length):
    if length > len(s) or length <= 0:
        return []
    mod = 10**9 + 7
    base = 131
    prefix_hash, pow_base = build_hash(s, base, mod)
    seen = {}
    duplicates = []
    added = set()
    for i in range(len(s) - length + 1):
        h = get_hash(prefix_hash, pow_base, i, i + length - 1, mod)
        sub = s[i:i + length]
        if h in seen:
            if sub not in added:
                duplicates.append(sub)
                added.add(sub)
        else:
            seen[h] = i
    return duplicates
