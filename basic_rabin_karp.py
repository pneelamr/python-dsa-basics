# Time: O(n+m) average (rare collisions), O(n*m) worst (all positions collide)
# Space: O(1) — only hash variables and index counters
def rabin_karp(text, pattern, base=256, mod=101):
    n = len(text)
    m = len(pattern)
    matches = []

    if m > n:
        return matches

    h = pow(base, m - 1, mod)
    pattern_hash = 0
    window_hash = 0

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:  # verify to handle hash collisions
                matches.append(i)

        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if window_hash < 0:
                window_hash += mod

    return matches
