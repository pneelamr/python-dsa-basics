def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        count[ch] = count.get(ch, 0) - 1
        if count[ch] < 0:
            return False
    return True


def find_anagrams(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    if m > n:
        return matches

    pattern_count = {}
    window_count = {}

    for ch in pattern:
        pattern_count[ch] = pattern_count.get(ch, 0) + 1
    for ch in text[:m]:
        window_count[ch] = window_count.get(ch, 0) + 1

    if pattern_count == window_count:
        matches.append(0)

    for i in range(m, n):
        ch_in = text[i]
        window_count[ch_in] = window_count.get(ch_in, 0) + 1

        ch_out = text[i - m]
        window_count[ch_out] -= 1
        if window_count[ch_out] == 0:
            del window_count[ch_out]

        if pattern_count == window_count:
            matches.append(i - m + 1)

    return matches
