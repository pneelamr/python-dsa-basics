# Z Algorithm: Computes the Z-array where Z[i] is the length of the longest substring starting at position i that matches a prefix of the string.
# Used for linear-time pattern matching by concatenating pattern + '$' + text and scanning the Z-array.
# O(n) time and space; conceptually similar to KMP but easier to implement.

# Time: O(n+m) — Z array built in linear time over concatenated string of length n+m+1
# Space: O(n+m) — Z array and concatenated string both of size n+m+1
def z_search(text, pattern):
    s = pattern + '$' + text
    n = len(s)
    m = len(pattern)
    z = _build_z(s)
    return [i - m - 1 for i in range(m + 1, n) if z[i] == m]


def _build_z(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0

    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]

    return z
