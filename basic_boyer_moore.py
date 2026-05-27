def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    if m > n:
        return matches

    bad_char = _bad_char_table(pattern)

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            matches.append(s)
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return matches


def _bad_char_table(pattern):
    table = {}
    for i, ch in enumerate(pattern):
        table[ch] = i
    return table
