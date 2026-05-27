# Suffix Array: Sorted array of all suffix start indices of a string, enabling O(m log n) pattern search.
# Built using prefix-doubling (O(n log² n)): sort suffixes by first 1, 2, 4, ... characters using rank arrays.
# LCP (Longest Common Prefix) array stores the length of the common prefix between consecutive suffixes in sorted order.

# Time: O(n log^2 n) — O(log n) doubling rounds each performing an O(n log n) sort
# Space: O(n) — rank and temporary arrays of length n
def build_suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    gap = 1
    while gap < n:
        def sort_key(i):
            return (rank[i], rank[i + gap] if i + gap < n else -1)
        sa.sort(key=sort_key)
        tmp[sa[0]] = 0
        for j in range(1, n):
            tmp[sa[j]] = tmp[sa[j - 1]]
            if sort_key(sa[j]) != sort_key(sa[j - 1]):
                tmp[sa[j]] += 1
        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        gap *= 2
    return sa

# Time: O(n) — Kasai's algorithm processes each suffix in amortized O(1) using the LCP invariant
# Space: O(n) — rank (inverse suffix array) and LCP arrays of length n
def build_lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i, v in enumerate(sa):
        rank[v] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

# Time: O(m log n) — binary search over n suffixes, each comparison takes O(m)
# Space: O(1) — constant extra space beyond inputs
def search(s, pattern, sa):
    m = len(pattern)
    n = len(s)

    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:sa[mid] + m] < pattern:
            lo = mid + 1
        else:
            hi = mid
    left = lo

    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:sa[mid] + m] <= pattern:
            lo = mid + 1
        else:
            hi = mid
    right = lo

    return [sa[i] for i in range(left, right)]
