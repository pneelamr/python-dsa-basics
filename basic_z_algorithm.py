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
