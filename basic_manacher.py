# Manacher's Algorithm: Finds all palindromic substrings in O(n) by exploiting symmetry of previously computed palindromes.
# Transform string by inserting separators (e.g. '#') to handle even/odd lengths uniformly.
# Maintain a center and right boundary; mirror known palindrome radii to avoid redundant expansion.

# Time: O(n) — each character is visited at most twice (once when right boundary expands, once when mirrored)
# Space: O(n) — transformed string and P array both length 2n+1
def manacher(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    center = 0
    right = 0
    for i in range(n):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
    return p

# Time: O(n) — one call to manacher then a single linear scan of P
# Space: O(n) — transformed string and P array
def longest_palindrome(s):
    p = manacher(s)
    t = '#' + '#'.join(s) + '#'
    best_len = 0
    best_center = 0
    for i, radius in enumerate(p):
        if radius > best_len:
            best_len = radius
            best_center = i
    start = (best_center - best_len) // 2
    return s[start:start + best_len]

# Time: O(n) — one call to manacher then a single linear scan of P
# Space: O(n) — transformed string and P array
def count_palindromes(s):
    p = manacher(s)
    total = 0
    for radius in p:
        total += (radius + 1) // 2
    return total
