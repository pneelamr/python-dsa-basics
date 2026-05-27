# Anagram: Two strings are anagrams if they contain exactly the same characters with the same frequencies.
# is_anagram uses a frequency dict; find_anagrams uses a sliding window with two dicts to find all anagram positions in a text.
# Both run in O(n) time and O(k) space where k is the alphabet size.

# Time: O(n) — iterates over each string once to build and check frequency counts
# Space: O(k) where k=alphabet size — count dict stores at most k distinct characters
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


# Time: O(n) — sliding window over text with O(1) dict comparison per step
# Space: O(k) where k=alphabet size — two frequency dicts of at most k entries each
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
