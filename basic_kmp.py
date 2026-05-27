# Knuth-Morris-Pratt (KMP): Linear-time string pattern search using a failure function (partial match table).
# The failure function encodes the longest proper prefix of the pattern that is also a suffix.
# On a mismatch, the pattern is shifted by the failure function value — no character in text is re-examined.

# Time: O(n+m) — linear scan of text (n) after O(m) LPS preprocessing
# Space: O(m) — LPS array of size m for the pattern
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = _build_lps(pattern)
    matches = []

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


def _build_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps
